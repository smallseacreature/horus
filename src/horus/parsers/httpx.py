import json
from pathlib import Path
from typing import Any

def process_httpx_jsonl(jsonl: Path, debug: bool = False) -> dict[str, Any]:

    """takes in the httpx output as jsonl, pulls relevant keys and outputs as dict for diff"""

    out: dict[str, Any] = {}

    if not jsonl.exists():
        if debug:
            print("no jsonl found")
        return out

    with jsonl.open("r", encoding="utf-8") as f:

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