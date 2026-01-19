#!/usr/bin/env python3
#v0.1.0

#imports
from __future__ import annotations

from horus.targets import process_target_list, diff_subdomains, diff_httpx
from horus.checks import preflight_checks
from horus.scanners import run_subfinder, run_httpx
from horus.output import discord_notify

#===============
# preflight
#===============
preflight_checks(True)

#===============
# loader
#===============
targets = process_target_list()

#===============
# collection/diff
#===============
for target in targets:
    run_subfinder(target)
    run_httpx(target)

    diff_httpx(target)
    diff_subdomains(target)

#===============
# alert
#===============
discord_notify("test alert")