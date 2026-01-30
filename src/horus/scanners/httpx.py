import horus.config as config
import subprocess     
import horus.file_manager.paths as paths

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
        "-H",  config.user_agent_header,
        "-H",  config.contact_header,
        "-o",  str(run_dir / "httpx.json")
        ]
    
    subdomains_file = run_dir / "subdomains.txt"
    if not subdomains_file.exists():
        raise FileNotFoundError(f"Missing {subdomains_file}")

    # Some CLI tools behave better if stdin ends with a newline
    stdin = subdomains_file.read_text(encoding="utf-8").strip() + "\n"
    
    result = subprocess.run(
        httpx_cmd,
        
        input          = stdin,
        text           = True,
        capture_output = True,
        check          = False
    )

    #CHAT CODE
    if result.returncode != 0:
        # include stderr to make debugging obvious
        raise RuntimeError(
            f"httpx failed (exit {result.returncode}). stderr:\n{result.stderr.strip()}"
        )