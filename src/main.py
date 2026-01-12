#!/usr/bin/env python3

#v0.1.0
                                                                  
                                                                          
# Structure: https://github.com/navdeep-G/samplemod

#This script is designed for reconnasiance on BugBounty targets. 

# take in a list of targets, check if there is already a folder for that target, if not, create it
# run a series of recon scripts on that target, rate limited, and including the hackerone header
# normalize all the  text
# see if there is a difference between them, if so, alert

#TODO 
# generate empty target list if targets does not exist
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

#imports
from __future__ import annotations

import os.path    #https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
import datetime   #https://stackoverflow.com/questions/3743222/how-do-i-convert-a-datetime-to-date
import subprocess #https://stackoverflow.com/questions/74763554/how-to-use-subprocess-run-method-in-python

#inits
targets = []

bug_bounty_header = "User-Agent: HackerOne-Research"
contact_header = "For issues please contact: smallseacreature@wearehackerone.com"

#Prgram start
print("H O R U S\n\n")

#process target list
print("[*] Processing target list...")
try:
    with open("./docs/targets.txt") as target_list:
        for line in target_list:
            targets.append(line.strip())

except FileNotFoundError as e:
    print(f"File Not Found: {e}")

print("[*] Done\n")

#run recon on each target
#see if folder exists

for target in targets:
    print(f"[*] starting diff on {target}")

    if os.path.isdir("./data/" + target) == False:
        print(f"[!] No folder for {target}")
        print(f"[*] Creating folder for {target}")
        os.makedirs(f"./data/{target}")

    #make new folder with timestamped name within target folder
    os.makedirs(f"./data/{target}/{datetime.datetime.now().date()}")

    #time to run some recon

    #SUBFINDER
    #[] avoids shell injection
    print("[*] Starting Subfinder")
    subfinder_cmd = [
        "subfinder", 
        "-d", target, 
        "-silent", #only outputs subdomains
    ]

    subfinder_output = subprocess.run(subfinder_cmd, capture_output=True, text=True)
    with open(f"./data/{target}/subdomains.txt", "w") as f:
        for line in subfinder_output.stdout.splitlines():
            f.write(line.strip() + "\n")

    print("[*] Subfinder Complete")


    #in order to diff, we should convert sections to sets, and compare sets
    def convert_to_set(file) -> set[Str]: 
        pass