import subprocess     
import horus.file_manager.paths as paths

def run_subfinder(target: str) -> None:
    
    """ Take in a target url and run subfinder on that url """

    output_file = paths.target_run_dir(target) / "subdomains.txt"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    subfinder_cmd = [
            "subfinder", 
            "-d", target, 
            "-silent",      #only outputs subdomains
        ]

    #run subfinder
    result = subprocess.run(
        subfinder_cmd, 
        capture_output=True, 
        text=True,
        check=False
        )

    #CHAT CODE
    if result.returncode != 0:
        raise RuntimeError(
            f"subfinder failed (exit {result.returncode}). stderr:\n{result.stderr.strip()}"
        )
    
    #write to file in data folder
    with output_file.open("w") as f:
        for line in result.stdout.splitlines():
            f.write(line.strip() + "\n")