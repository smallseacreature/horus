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
import os.path                     
              


from horus.targets import process_target_list, convert_to_set, jsonl_to_dict
from horus.checks import program_start, check_command
import horus.config as config
