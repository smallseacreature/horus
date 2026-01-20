import horus.config as config
import subprocess     
import horus.paths as paths



def run_subfinder(target: str, debug: bool = False) -> None:
    
    """intake a target, places a list of subdomains in ./data/{target}"""

    if debug:
        print(f"Starting subfinder on {target}")
        
    out_file = paths.target_run_dir(target) / "subdomains.txt"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    
    subfinder_cmd = [
            "subfinder", 
            "-d", target, 
            "-silent",      #only outputs subdomains
        ]

    #run subfinder
    result = subprocess.run(
        subfinder_cmd, 
        capture_output=True, 
        text=True
        )

    #write to file in data folder
    with out_file.open("w") as f:
        for line in result.stdout.splitlines():
            f.write(line.strip() + "\n")