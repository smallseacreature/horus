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

#imports
from __future__ import annotations

import os.path    #https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
import datetime   #https://stackoverflow.com/questions/3743222/how-do-i-convert-a-datetime-to-date
import subprocess #https://stackoverflow.com/questions/74763554/how-to-use-subprocess-run-method-in-python

#inits
targets = []

bug_bounty_header = "User-Agent: HackerOne-Research"
contact_header = "For issues please contact: smallseacreature@wearehackerone.com"

#process target list
try:
    with open("./docs/targets.txt") as target_list:
        for line in target_list:
            targets.append(line.strip())

except FileNotFoundError as e:
    print(f"File Not Found: {e}")

#run recon on each target
#see if folder exists
for target in targets:
    if os.path.isdir("./data/" + target) == False:
        print(f"[!] No folder for {target}")
        print(f"[*] Creating folder for {target}")
        os.makedirs(f"./data/{target}")

    #make new folder with timestamped name within target folder
    os.makedirs(f"./data/{target}/{datetime.datetime.now().date()}")

    #time to run some recon

    #SUBFINDER
    #[] avoids shell injection

    subfinder_cmd = [
        "subfinder", 
        "-d", target, 
        "-silent", #only outputs subdomains
    ]

    subfinder_output = subprocess.run(subfinder_cmd, capture_output=True, text=True)
    print(subfinder_output)



