#loader.py
import paths
from pathlib import Path

def process_target_list(debug=False):

    """ Processes target list at filepath into a list """

    if debug:
        print("Processing target list")

    targets = [] # empty list for valid targets

    filepath = "./targets/targets.txt"
    targets_file = Path(filepath)

    #creates list object from targets file
    if targets_file.is_file():
        with open(targets_file) as f:
            for raw in f:
                line = raw.strip()

                if not line:
                    continue

                if line.startswith("Enter in website names"):
                    print("[!] Remove default message in targets list")
                    continue

                if "://" in line or "/" in line:
                    print(f"[!] Skipping invalid target: {line}")
                    continue

                targets.append(line)

        if not targets:
            print("[!] No targets in target list")
            return None
        
    #creates file if it does not exist (for some reason)     
    else:
        print(f"The file '{filepath}' does not exist or is not a regular file.")
        print("Creating file for you...")
        with open("./docs/targets.txt", "x") as target_list:
            target_list.write("Enter in website names, ie 'google.com', seperated by newlines")
        print("Targets.txt created in ./docs")
        return None
    
    return targets