import horus.file_manager.paths as paths
from pathlib import Path

def read_lines(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def diff_subfinder(target: str):

    messages = {}

    
    state_dir = paths.target_state_dir(target)
    run_dir   = paths.target_run_dir(target)

    #if there is no state, exit 
    if not (state_dir / "subdomains.txt").is_file():
        return messages
    
    #convert subdomains to sets
    run_set   = read_lines(run_dir   / "subdomains.txt")
    state_set = read_lines(state_dir / "subdomains.txt")

    #lists of added/removed
    added   = sorted(run_set - state_set)
    removed = sorted(state_set - run_set)

    #build messages
    for subdomain in added:
        messages[subdomain] = [f"[+] {subdomain} added"]

    for subdomain in removed:
        messages[subdomain] = [f"[-] {subdomain} removed"]

    return messages