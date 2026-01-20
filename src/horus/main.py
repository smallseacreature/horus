#!/usr/bin/env python3
#v0.1.0

#imports
from __future__ import annotations

from horus.targets import process_target_list, diff_subdomains, diff_httpx, update_target_state
from horus.checks import preflight_checks
from horus.scanners import run_subfinder, run_httpx
from horus.output import discord_notify

DEBUG = True

def main() -> int:
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
        run_subfinder(target, DEBUG)
        run_httpx(target)

        subdomain_alerts = diff_subdomains(target)
        httpx_alerts = diff_httpx(target)

        discord_notify(subdomain_alerts)
        discord_notify(httpx_alerts)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())