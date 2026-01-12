#!/usr/bin/env python3

#v0.1.0
                                                                  
                                                                          
# Structure: https://github.com/navdeep-G/samplemod

#This script is designed for reconnasiance on BugBounty targets. 

# take in a list of targets, check if there is already a folder for that target, if not, create it
# run a series of recon scripts on that target, rate limited, and including the hackerone header
# normalize all the  text
# see if there is a difference between them, if so, alert

#TODO 
# look in current directory for likely files if targets does not exist
# clean targets list before placing in list
# make code comments fancier, better organization
# warn if an old folder has not been checked 
# record the precise time in the JSON output
# check if the command exists first 
# modulize ts 
# throw error if the target syntax is invalid
# maybe switch os to pathlib 
# the datetime folder creation needs to check if 
# correct datetime, probably just fix it yourself
# clean all text at input
# handle already having a folder for the day
# check if email has not been changed
# check if exit() is the right move there
# handle no folder for yesterday

#imports
from __future__ import annotations

import os.path    #https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
import subprocess #https://stackoverflow.com/questions/74763554/how-to-use-subprocess-run-method-in-python
from datetime import date, timedelta


#Constants
DATE_TODAY = date.today()
DATE_YESTERDAY = date.today() - timedelta(days=1)

RATE_LIMIT = 25

#in order to diff, we should convert sections to sets, and compare sets
def convert_to_set(file: str) -> set[str]: 

    """converts file at filepath to a set"""

    out = set()
    with open(file) as f:
        for line in f:
            out.add(line.strip())
    
    return out


#inits
targets = []
bug_bounty_header = "User-Agent: HackerOne-Research"
contact_header = "X-Contact: smallseacreature@wearehackerone.com"

#Prgram start
print("\nH O R U S\n")

#process target list
print("[*] Processing target list...")
try:
    with open("./docs/targets.txt") as target_list:
        for line in target_list:
            if line == "Enter in website names, ie 'google.com', seperated by newlines":
                print("Please edit target list")
                exit()
            targets.append(line.strip())

except FileNotFoundError as e:
    print(f"File Not Found: {e}")
    with open("./docs/targets.txt", "x") as target_list:
        target_list.write("Enter in website names, ie 'google.com', seperated by newlines")
    print("Targets.txt created in ./docs")

print("[*] Done\n")

#run recon on each target
#see if folder exists

for target in targets:
    print(f"[*] starting diff on {target}")

    if os.path.isdir("./data/" + target) == False:
        print(f"[!] No folder for {target}")
        print(f"[*] Creating folder for {target}")
        os.makedirs(f"./data/{target}")

    try:
        #make new folder with timestamped name within target folder
        os.makedirs(f"./data/{target}/{DATE_TODAY}")
    except FileExistsError as e:
        print(f"Error: {e}, file will be overwritten")

    #time to run some recon

    #SUBFINDER
    #[] avoids shell injection
    print(f"[*] Starting Subfinder on {target}")
    subfinder_cmd = [
        "subfinder", 
        "-d", target, 
        "-silent", #only outputs subdomains
    ]

    #run subfinder
    subfinder_output = subprocess.run(subfinder_cmd, capture_output=True, text=True)

    with open(f"./data/{target}/{DATE_TODAY}/subdomains.txt", "w") as f:
        for line in subfinder_output.stdout.splitlines():
            f.write(line.strip() + "\n")

    print("[*] Subfinder Complete")

    #convert old file to set, convert new file to set, compare
    todays_subdomains     = convert_to_set(f"./data/{target}/{DATE_TODAY}/subdomains.txt")
    yesterdays_subdomains = convert_to_set(f"./data/{target}/{DATE_YESTERDAY}/subdomains.txt")

    if todays_subdomains == yesterdays_subdomains:
        print("they are the same")
    else:
        print("different")

    #run httpx on todays subdomains
    print(f"[*] Starting httpx on {target} subdomains")
    cmd = [
    "httpx",
    "-silent",
    "-sc",
    "-title",
    "-td",
    "-fr",
    "-j",
    "-rl", str(RATE_LIMIT),
    "-H", bug_bounty_header,
    "-H", contact_header,
    "-o", f"./data/{target}/{DATE_TODAY}/httpx.json"
    ]

    result = subprocess.run(
        cmd,
        input="\n".join(todays_subdomains),
        text=True,
        capture_output=True,
        check=False,
    )
