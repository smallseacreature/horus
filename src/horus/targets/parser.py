#parser.py
import json
from pathlib import Path
from typing import Any
import re
from typing import Optional, Tuple
from horus.output import no_embed
#=========================
# Simple Conversions
#=========================

def convert_to_set(file: Path) -> set[str]: 

    """converts file at filepath to a set"""

    out = set()
    with open(file) as f:
        for line in f:
            out.add(line.strip())
    
    return out

#=========================
# Json Processor
#=========================

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

#=========================
# DeepDiff subfinder Processor
#=========================

def subfinder_lists_to_message(subdomains_added, subdomains_removed) -> str:
    lines: list[str] = []

    if not subdomains_added:
        lines.append(f"No subdomains added")
    else:
        for added in subdomains_added:
            lines.append(f"[+] Subdomains added {added}")

    if not subdomains_removed:
        lines.append(f"No subdomains removed")
    else:
        for removed in subdomains_added:
            lines.append(f"[-] Subdomains removed {removed}")

    return "\n".join(lines)

#=========================
# DeepDiff httpx Processor
#=========================

#TODO this whole section needs rework to ouput correctly


