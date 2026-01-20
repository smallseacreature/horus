#parser.py
import json
from pathlib import Path
from typing import Any

def convert_to_set(file: Path) -> set[str]: 

    """converts file at filepath to a set"""

    out = set()
    with open(file) as f:
        for line in f:
            out.add(line.strip())
    
    return out

def jsonl_to_dict(path: Path) -> dict[str, Any]:
    """
    Reads a JSONL file (one JSON object per line) and returns a dict keyed by something.
    Adjust the key logic depending on your schema.
    """
    out: dict[str, Any] = {}

    if not path.exists():
        return out  # or raise, depending on your workflow

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)         
            # Pick a stable key for diffing. Examples:
            # key = obj.get("input") or obj.get("host") or obj.get("url")
            key = obj.get("url") or obj.get("input") or obj.get("host")
            if key is None:
                continue
            out[str(key)] = obj

    return out