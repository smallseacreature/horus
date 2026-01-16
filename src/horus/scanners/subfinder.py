import horus.config as config
import subprocess     

def run_subfinder(target):
    
    """intake a target, places a list of subdomains in ./data/{target}"""

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
    with open(f"./data/{target}/{config.DATE_TODAY}/subdomains.txt", "w") as f:
        for line in result.stdout.splitlines():
            f.write(line.strip() + "\n")