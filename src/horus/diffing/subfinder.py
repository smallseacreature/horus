import horus.diffing.file_manager.paths as paths
from horus.targets import convert_to_set

def diff_subfinder(target: str):

    messages = {}

    state_dir = paths.target_state_dir(target)
    run_dir   = paths.target_run_dir(target)

    run_subdomains   = convert_to_set(run_dir   / "subdomains.txt")

    if ((state_dir / "subdomains.txt").is_file()):
        state_subdomains = convert_to_set(state_dir / "subdomains.txt")
    else:
        return messages

    for subdomain in run_subdomains:
        if subdomain not in state_subdomains:
            messages[subdomain] = [f"[+] {subdomain} added"]

    for subdomain in state_subdomains:
        if subdomain not in run_subdomains:
            messages[subdomain] = [f"[-] {subdomain} removed"]

    return messages