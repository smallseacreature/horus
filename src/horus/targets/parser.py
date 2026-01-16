#parser.py
import json

def convert_to_set(file: str) -> set[str]: 

    """converts file at filepath to a set"""

    out = set()
    with open(file) as f:
        for line in f:
            out.add(line.strip())
    
    return out

def jsonl_to_dict(jsonl: str) -> dict:

    """ convert json lines file at filepath to a python dictionary """

    out: dict = json.loads(jsonl)
    return(out)