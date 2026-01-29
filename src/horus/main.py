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
    output_message = []

    output_message.append("************HORUS************")
    output_message.append(f"Date: {config.DATE_TODAY}\n")

    for target in targets:

        run_subfinder(target)
        run_httpx(target)
        
        #TODO change all from subdomain to subfinder for consistent naming
        subdomain_messages = diff_subdomains(target)
        httpx_messages     = diff_httpx(target)

        output_message.append(f"RESULTS FOR: {target}\n")

        if subdomain_messages:
            output_message.append("Changes found with Subfinder:\n")
            if len(subdomain_messages) > config.MAX_DISCORD_MESSAGES:
                output_message.append(f"[!] There are {len(subdomain_messages)} subfinder results changed\n")
            print(subdomain_messages.items())
                
        else:
            output_message.append("No changes to subfinder results\n")

        #TODO fix messaging
        if httpx_messages:
            output_message.append("Changes found with httpx:\n")
            if len(httpx_messages) > config.MAX_DISCORD_MESSAGES:
                output_message.append(f"[!] There are {len(httpx_messages)} httpx results changed")
            else:
                for url, msgs in httpx_messages.items():
                    for msg in msgs:
                        output_message.append(msg)
        else:
            output_message.append("No changes to httpx results\n")
    
    output_message.append("_________________________\n")
    
    output_message = "\n".join(output_message)
    
    discord_notify(output_message)

if __name__ == "__main__":
    raise SystemExit(main())