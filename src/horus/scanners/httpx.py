import horus.config as config
import subprocess     
import horus.diffing.file_manager.paths as paths
from horus.targets.parser import convert_to_set

def run_httpx(target: str) -> None:

    """ Take in a target url and run httpx on that url """

    run_dir = paths.target_run_dir(target)

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
        "-o", str(run_dir / "httpx.json")
        ]
    
    #TODO investigate convert to set memory impact
    result = subprocess.run(
        httpx_cmd,
        # Some CLI tools behave better if stdin ends with a newline
        input="\n".join(convert_to_set(run_dir / "subdomains.txt")) + "\n",
        text=True,
        capture_output=True,
        check=False
    )

    #CHAT CODE
    if result.returncode != 0:
        # include stderr to make debugging obvious
        raise RuntimeError(
            f"httpx failed (exit {result.returncode}). stderr:\n{result.stderr.strip()}"
        )