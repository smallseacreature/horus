#!/usr/bin/env python3
#v0.1.0

#imports
from __future__ import annotations

from horus.targets      import process_target_list
from horus.diffing      import diff_subfinder, diff_httpx
from horus.checks       import run_preflight_checks
from horus.scanners     import run_subfinder, run_httpx
from horus.output       import discord_notify, httpx_social_output, subfinder_social_output, \
                               output_httpx_data, output_subfinder_data
from horus.file_manager import update_target_state, target_run_dir
import horus.config     as config


def main():
    #===============
    # preflight
    #===============
    run_preflight_checks()

    #===============
    # loader
    #===============
    targets = process_target_list()

    #===============
    # diff
    #===============
    output_message = []

    # Header
    output_message.append("**HORUS**\n")
    output_message.append(f"Date: {config.DATE_TODAY}\n")

    #Start by target
    for target in targets:

        #run tools on target
        if not (target_run_dir(target) / "subdomains.txt").is_file():
            run_subfinder(target)

        if not (target_run_dir(target) / "httpx.json").is_file():   
            run_httpx(target)
  
        #diff
        httpx_diff_result     = diff_httpx(target)
        subfinder_diff_result = diff_subfinder(target)

        httpx_social_output_result     = httpx_social_output(httpx_diff_result)
        subfinder_social_output_result = subfinder_social_output(subfinder_diff_result)

        output_message.append(f"RESULTS FOR: {target}")
        output_message.append(httpx_social_output_result)
        output_message.append(subfinder_social_output_result)
    
    output_message.append("_\n")
    
    # build and notify
    output_message = "\n".join(output_message)
    discord_notify(output_message)

    #write data
    output_httpx_data(httpx_diff_result, target)
    output_subfinder_data(subfinder_diff_result, target)
    #move to state
    update_target_state(target)

if __name__ == "__main__":
    raise SystemExit(main())