import horus.config as config
import subprocess     
import horus.paths as paths
from horus.targets.parser import convert_to_set

def run_httpx(target: str):

    run_dir = paths.target_run_dir(target)
    state_dir = paths.target_state_dir(target)

    """ take in a Set of subdomains, and the folder to place it in"""
    httpx_cmd = [
        "httpx",
        "-silent",
        "-sc",
        "-title",
        "-td",
        "-fr",
        "-j",
        "-rl", str(config.RATE_LIMIT),
        "-H", config.bug_bounty_header,
        "-H", config.contact_header,
        "-o", run_dir / "httpx.json"
        ]
    
    subprocess.run(
        httpx_cmd,
        input="\n".join(convert_to_set(run_dir / "subdomains.txt")),
        text=True,
        capture_output=True,
        check=False,
    )