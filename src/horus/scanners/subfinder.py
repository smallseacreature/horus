import horus.config as config
import subprocess     
import horus.paths as paths



def run_subfinder(target):
    
    """intake a target, places a list of subdomains in ./data/{target}"""

    run_dir = paths.target_run_dir(target)
    
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
    with open(run_dir / "subdomains.txt", "w") as f:
        for line in result.stdout.splitlines():
            f.write(line.strip() + "\n")