import horus.diffing.file_manager.paths as paths
from horus.targets import process_httpx_jsonl

def diff_httpx(target: str):

    """takes in 2 processed httpx dicts, output messages as difference"""

    messages     = {}

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