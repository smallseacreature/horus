#!/usr/bin/env python3
#v0.1.0

#imports
from __future__ import annotations

from horus.targets import process_target_list, diff_subdomains, diff_httpx
from horus.checks import preflight_checks
from horus.scanners import run_subfinder, run_httpx
from horus.output import discord_notify

DEBUG = True

def main():
    #===============
    # preflight
    #===============
    preflight_checks(DEBUG)

    #===============
    # loader
    #===============
    targets = process_target_list(DEBUG)

    #===============
    # diff
    #===============


    for target in targets:

        run_subfinder(target)
        run_httpx(target)
        
        subdomain_messages = diff_subdomains(target)
        httpx_messages = diff_httpx(target)
    
        print(subdomain_messages)
        print(httpx_messages)
        
        

if __name__ == "__main__":
    raise SystemExit(main())