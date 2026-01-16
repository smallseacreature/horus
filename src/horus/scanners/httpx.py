import horus.config as config
import subprocess     

def run_httpx(subdomains: set, target_folder: str):

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
        "-o", f"./data/{target_folder}/{config.DATE_TODAY}/httpx.json"
        ]
    
    result = subprocess.run(
        httpx_cmd,
        input="\n".join(subdomains),
        text=True,
        capture_output=True,
        check=False,
    )