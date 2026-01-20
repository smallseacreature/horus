from __future__ import annotations

from .parser import convert_to_set, process_httpx_jsonl
import horus.paths as paths
from pathlib import Path
import shutil
from deepdiff import DeepDiff

DEBUG = True

def process_httpx_diff(diff) -> tuple[list, list]:

    """converts deepdiff output to items """
    items_removed = [] #the httpx probe failed where it once succeeded 
    items_added   = [] #new live hosts


    if "dictionary_item_removed" in diff:
        items_removed.extend(diff["dictionary_item_removed"])

    if 'dictionary_item_added' in diff:
        items_added.extend(diff['dictionary_item_added'])

    if 'values_changed' in diff:
        for change in diff:
            url = change.get('root')
            old_value = change.get('old_value')
            new_value = change.get('new_value')

    return items_added, items_removed

def process_subfinder_diff(diff: DeepDiff) -> tuple[list, list]:

    """converts subfinder DeepDiff to list of added and removed"""

    subdomains_removed = []
    subdomains_added   = []

    if "dictionary_item_removed" in diff:
        subdomains_removed.extend(diff["dictionary_item_removed"])

    if 'dictionary_item_added' in diff:
        subdomains_added.extend(diff['dictionary_item_added'])
    
    return subdomains_removed, subdomains_added
     
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

    """copy the targets run data into the state data, overwriting the previous state"""
    state_dir = paths.target_state_dir(target)
    run_dir = paths.target_run_dir(target)

    copy_dir_contents(run_dir, state_dir)

#diff logic for data that already exists within ./data

def diff_subdomains(target: str, debug: bool = False):

    state_dir = paths.target_state_dir(target)
    run_dir   = paths.target_run_dir(target)

    state_dir = convert_to_set(state_dir)
    run_dir   = convert_to_set(run_dir)
    
    diff = DeepDiff(state_dir, run_dir)



def diff_httpx(target):
    # we care about keys url, tech and status code

    state_dir = paths.target_state_dir(target)
    run_dir   = paths.target_run_dir(target)

    # load JSONL into dicts for diffing
    run_httpx     = process_httpx_jsonl(state_dir / "httpx.json", DEBUG)
    state_httpx   = process_httpx_jsonl(run_dir / "httpx.json", DEBUG)

    run_httpx = sorted(run_httpx)
    state_httpx = sorted(state_httpx)

    diff = DeepDiff(state_httpx, run_httpx)

    print(diff)
    

