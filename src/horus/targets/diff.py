from __future__ import annotations

from .parser import convert_to_set, process_httpx_jsonl
import horus.paths as paths
from pathlib import Path
import shutil

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

def diff_subdomains(target: str, debug: bool = False):

    messages = {}

    state_dir = paths.target_state_dir(target)
    run_dir   = paths.target_run_dir(target)

    state_subdomains = convert_to_set(state_dir / "subdomains.txt")
    run_subdomains   = convert_to_set(run_dir   / "subdomains.txt")

    for subdomain in run_subdomains:
        if subdomain not in state_subdomains:
            messages[subdomain] = [f"[+] {subdomain} added"]

    for subdomain in state_subdomains:
        if subdomain not in run_subdomains:
            messages[subdomain] = [f"[-] {subdomain} removed"]

    return messages
#====================
# httpx
#====================

def diff_httpx(target: str):

    """takes in 2 processed httpx dicts, output messages as difference"""

    messages     = {}
    urls_added   = []
    urls_removed = []

    run_dir   = paths.target_run_dir(target)
    state_dir = paths.target_state_dir(target)

    run   = process_httpx_jsonl(run_dir   / "httpx.json")
    state = process_httpx_jsonl(state_dir / "httpx.json")
    for url in run:
        if url in state:  # Pull info from each url shared with the state

            run_status_code   = run[url].get("status_code")
            state_status_code = state[url].get("status_code")

            if run_status_code != state_status_code:
                status_code_msg = (
                    f"[~] {url} status changed {state_status_code} → {run_status_code}"
                )
            else:
                status_code_msg = None


            run_title   = run[url].get("title")
            state_title = state[url].get("title")

            if run_title != state_title:
                title_msg = (
                    f"[~] <{url}> title changed {state_title} → {run_title}"
                )
            else:
                title_msg = None
            
            run_tech   = run[url].get("tech")
            state_tech = state[url].get("tech")

            techs_added = []
            techs_removed = []

            if run_tech:
                for tech in run_tech:
                    if tech not in state_tech:
                        techs_added.append(tech)
            
            if state_tech:
                for tech in state_tech:
                    if tech not in run_tech:
                        techs_removed.append(tech)

            if techs_added:
                techs_added_msg = f"[+] Techs added: {', '.join(techs_added)}"
            else:
                techs_added_msg = None

            if techs_removed:
                techs_removed_msg = f"[-] Techs removed: {', '.join(techs_removed)}"
            else:
                techs_removed_msg = None

            msgs = [
            m for m in (
                status_code_msg,
                title_msg,
                techs_added_msg,
                techs_removed_msg
            )
            if m
            ]
            if msgs:
                messages[url] = msgs

        else:             # URL is not in state, add to URLs added
            messages[url] = [f"[+] {url} added"]
    for url in state:

        if url not in run:
            messages[url] = [f"[-] {url} removed"]
    
    return messages