#parser.py
import json
from pathlib import Path
from typing import Any
import re
from typing import Optional, Tuple

#====================
# Simple Conversions
#====================

def convert_to_set(file: Path) -> set[str]: 

    """converts file at filepath to a set"""

    out = set()
    with open(file) as f:
        for line in f:
            out.add(line.strip())
    
    return out

#====================
# Json Processor
#====================

def process_httpx_jsonl(jsonl: Path, debug: bool = False) -> dict[str, Any]:

    """takes in the httpx output as jsonl, pulls relevant keys and outputs as dict for diff"""

    out: dict[str, Any] = {}

    if not jsonl.exists():
        if debug:
            print("no jsonl found")
        return out

    with jsonl.open("r", encoding="utf-8") as f:

        if debug:
            print("opening jsonl")

        for line in f:
            line = line.strip()
            if not line:
                continue

            httpx_result = json.loads(line)

            url = httpx_result.get("url")
            if not url:
                continue

            status_code = httpx_result.get("status_code")
            if status_code is None:
                continue

            tech = httpx_result.get("tech") or []
            if not isinstance(tech, list):
                tech = [str(tech)]
            tech_norm = tuple(sorted(str(t) for t in tech))

            out[str(url)] = {"status_code": str(status_code), "tech": tech_norm}

    return out

#====================
# DeepDiff Processor
#====================

#RE Statements
URL_RE   = re.compile(r"root\['(?P<url>https?://[^']+)'\]")
FIELD_RE = re.compile(r"\]\['(?P<field>[^']+)'\]")   # grabs dict fields like ['tech']
INDEX_RE = re.compile(r"\[(?P<idx>\d+)\]$")          # trailing [0]

def parse_path(path: str) -> Tuple[Optional[str], Optional[str], Optional[int]]:
    """
    Examples:
      root['https://www.newegg.com']
      root['https://eniac.newegg.com']['tech'][0]
    Returns: (url, field, index)
    """
    url_m = URL_RE.search(path)
    url = url_m.group("url") if url_m else None

    fields = FIELD_RE.findall(path)
    field = fields[-1] if fields else None

    idx_m = INDEX_RE.search(path)
    idx = int(idx_m.group("idx")) if idx_m else None

    return url, field, idx

def deepdiff_to_events(diff: dict) -> list[dict]:
    events: list[dict] = []

    # removed URLs/keys
    for path in diff.get("dictionary_item_removed", []):
        url, _, _ = parse_path(path)
        events.append({"type": "URL_REMOVED", "url": url or path})

    # values changed (old/new payload)
    for path, payload in diff.get("values_changed", {}).items():
        url, field, idx = parse_path(path)
        events.append({
            "type": "VALUE_CHANGED",
            "url": url or path,
            "field": field,
            "index": idx,
            "old": payload.get("old_value"),
            "new": payload.get("new_value"),
        })

    # list element added
    for path, value in diff.get("iterable_item_added", {}).items():
        url, field, idx = parse_path(path)
        events.append({
            "type": "ITEM_ADDED",
            "url": url or path,
            "field": field,
            "index": idx,
            "value": value,
        })

    # list element removed
    for path, value in diff.get("iterable_item_removed", {}).items():
        url, field, idx = parse_path(path)
        events.append({
            "type": "ITEM_REMOVED",
            "url": url or path,
            "field": field,
            "index": idx,
            "value": value,
        })

    return events

def events_to_message(events: list[dict], max_lines: int = 20) -> str:
    lines: list[str] = []

    for e in events:
        t = e["type"]

        if t == "URL_REMOVED":
            lines.append(f"[-] httpx missing: {e['url']}")

        elif t == "VALUE_CHANGED":
            # Example: tech[0]: Akamai -> Cloudflare
            field = e.get("field") or "value"
            idx = e.get("index")
            idx_s = f"[{idx}]" if idx is not None else ""
            lines.append(f"[~] {e['url']} {field}{idx_s}: {e['old']} → {e['new']}")

        elif t == "ITEM_ADDED":
            field = e.get("field") or "item"
            idx = e.get("index")
            idx_s = f"[{idx}]" if idx is not None else ""
            lines.append(f"[+] {e['url']} {field}{idx_s} added: {e['value']}")

        elif t == "ITEM_REMOVED":
            field = e.get("field") or "item"
            idx = e.get("index")
            idx_s = f"[{idx}]" if idx is not None else ""
            lines.append(f"[-] {e['url']} {field}{idx_s} removed: {e['value']}")

    # avoid spamming Discord
    if len(lines) > max_lines:
        extra = len(lines) - max_lines
        lines = lines[:max_lines]
        lines.append(f"...and {extra} more changes")

    return "\n".join(lines) if lines else "No changes detected."
