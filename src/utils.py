#in order to diff, we should convert sections to sets, and compare sets
from shutil import which
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

def check_command(command):
    """ return T/F on commands existence """
    if which(command) == None:
        return False
    else:
        return True