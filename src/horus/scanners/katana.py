import subprocess
from pathlib import Path
from horus.file_manager import target_run_dir
from horus.parsers import process_httpx_jsonl

def live_hosts(httpx_json):

    httpx_output = process_httpx_jsonl(httpx_json)

    #out[str(url)] = {"status_code": str(status_code), "tech": tech_norm}
    
    for url in httpx_output.keys():
        if httpx_output.get


def run_katana(target: str) -> None:

    run_dir = target_run_dir(target)
    hosts_file = run_dir / "hosts.txt"
    out_file = run_dir / "katana.jsonl"

    if not hosts_file.exists():
        # nothing to crawl
        return out_file

    cmd = [
        "katana",
        "-silent",
        "-jsonl",
        "-d", "2",          # depth (start small)
        "-rl", "5",         # rate limit
        "-c", "5",          # concurrency
        "-follow-redirects",
        "-o", str(out_file),
    ]

    stdin = hosts_file.read_text(encoding="utf-8").strip() + "\n"
    result = subprocess.run(
        cmd,
        input=stdin,
        text=True,
        capture_output=not debug,
    )

    if result.returncode != 0:
        raise RuntimeError(f"katana failed: {result.stderr.strip()}")

    return out_file