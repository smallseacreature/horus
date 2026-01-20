from __future__ import annotations

from .parser import convert_to_set, process_httpx_jsonl, httpx_deepdiff_to_events, httpx_events_to_message, \
                    subfinder_lists_to_message
import horus.paths as paths
from pathlib import Path
import shutil
from deepdiff import DeepDiff

DEBUG = True

#====================
# Helper Functions
#====================

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

#====================
# Subdomains
#====================

def subdomains_to_DeepDiff(target: str, debug: bool = False):

    state_dir = paths.target_state_dir(target)
    run_dir   = paths.target_run_dir(target)

    state_dir = convert_to_set(state_dir / "subdomains.txt")
    run_dir   = convert_to_set(run_dir / "subdomains.txt")
    
    diff = DeepDiff(state_dir, run_dir)

    return diff

def diff_subdomains(target) -> str:

    subdomains_added   = []
    subdomains_removed = []

    diff = subdomains_to_DeepDiff(target)

    if "dictionary_item_added" in diff.keys():
        subdomains_added.extend(diff["dictionary_item_added"])
        
    if "dictionary_item_removed" in diff.keys():
        subdomains_removed.extend(diff["dictionary_item_removed"])

    subdomain_messages = subfinder_lists_to_message(subdomains_added, subdomains_removed)

    return subdomain_messages

#====================
# httpx
#====================

def httpx_to_DeepDiff(target):
    # we care about keys url, tech and status code

    state_dir = paths.target_state_dir(target)
    run_dir   = paths.target_run_dir(target)

    # load JSONL into dicts for diffing
    run_httpx     = process_httpx_jsonl(state_dir / "httpx.json", DEBUG)
    state_httpx   = process_httpx_jsonl(run_dir / "httpx.json", DEBUG)

    run_httpx = sorted(run_httpx)
    state_httpx = sorted(state_httpx)

    diff = DeepDiff(state_httpx, run_httpx)

    return diff

def diff_httpx(target) -> str:

    """diff the httpx of a target, output the messages for discord """

    httpx_diff      = httpx_to_DeepDiff(target)
    httpx_events    = httpx_deepdiff_to_events(httpx_diff)
    httpx_messages  = httpx_events_to_message(httpx_events)

    return httpx_messages