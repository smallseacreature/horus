from __future__ import annotations

from .parser import convert_to_set, jsonl_to_dict
import horus.paths as paths
from pathlib import Path
import shutil

def check_for_state(target: str, debug:bool = False) -> bool:

    """ return bool on state directories existence in target folder"""

    state_dir = paths.target_state_dir(target)

    return state_dir.is_dir()


def copy_dir_contents(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)

    for item in src.iterdir():
        if item.is_file():
            shutil.copy2(item, dst / item.name)

def update_target_state(target: str, debug: bool = False):
    #TODO finish this
    state_dir = paths.target_state_dir(target)
    run_dir = paths.target_run_dir(target)
     
#diff logic for data that already exists within ./data
def diff_subdomains(target: str, debug: bool = False):

    state_dir = paths.target_state_dir(target)
    run_dir = paths.target_run_dir(target)

    if state_dir.is_dir():
        state_subdomains = convert_to_set(state_dir / "subdomains.txt")
    else:
         state_subdomains = None
    new_subdomains = convert_to_set(run_dir / "subdomains.txt")
    
    if state_subdomains:
            if new_subdomains == state_subdomains:
                print("they are the same")
            else:
                print("different")
    else:
         print(f"First run on {target}")
    #convert old file to set, convert new file to set, compare

def diff_httpx(target):

    state_dir = paths.target_state_dir(target)
    run_dir = paths.target_run_dir(target)

    # load JSONL into structured data for diffing
    new_httpx     = jsonl_to_dict(state_dir / "httpx.json")
    state_httpx   = jsonl_to_dict(run_dir / "httpx.json")

    print(new_httpx.keys())

