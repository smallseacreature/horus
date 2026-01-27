#!/usr/bin/env python3
#v0.1.0

#imports
from __future__ import annotations

from horus.targets import process_target_list, diff_subdomains, diff_httpx
from horus.checks import preflight_checks
from horus.scanners import run_subfinder, run_httpx
from horus.output import discord_notify
import horus.config as config

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

    discord_notify("************HORUS************")
    discord_notify(f"Date: {config.DATE_TODAY}")
    discord_notify(" ")

    for target in targets:

        run_subfinder(target)
        run_httpx(target)
        
        #TODO change all from subdomain to subfinder for consistent naming
        subdomain_messages = diff_subdomains(target)
        httpx_messages     = diff_httpx(target)

        discord_notify(f"RESULTS FOR: {target}")

        if subdomain_messages:
            discord_notify("Changes found with Subfinder:")
            if len(subdomain_messages) > config.MAX_DISCORD_MESSAGES:
                discord_notify(f"[!] There are {len(subdomain_messages)} subfinder results changed")
            for url, msgs in subdomain_messages.items():
                for msg in msgs:
                    discord_notify(msg)
        else:
            discord_notify("No changes to subfinder results")

        #TODO fix messaging
        if httpx_messages:
            discord_notify("Changes found with httpx:")
            if len(httpx_messages) > config.MAX_DISCORD_MESSAGES:
                discord_notify(f"[!] There are {len(httpx_messages)} httpx results changed")
            else:
                for url, msgs in httpx_messages.items():
                    for msg in msgs:
                        discord_notify(msg)
        else:
            discord_notify("No changes to httpx results")
    
    discord_notify("_________________________")
            
if __name__ == "__main__":
    raise SystemExit(main())