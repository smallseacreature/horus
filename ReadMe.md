# Niffler
<p> A Docker-first reconnaissance and change-detection pipeline for bug bounty and security research. <p>

<p> This tool runs passive subdomain enumeration, probes live HTTP(S) services, stores historical snapshots, diffs results between runs, and sends Discord alerts. <p>

<p>Designed to run in a homelab using Docker + cron/systemd.

## Features
- Passive subdomain enumeration using subfinder
- Live HTTP(S) probing using httpx
- Timestamped historical runs
- Stable state snapshots for reliable diffs
- Added / removed detection (no noisy reordering diffs)
- Optional Discord webhook notifications
- Safe for automation (no shell execution, fail-soft behavior)
- Docker-first (host stays clean)

## Key directories
- targets/
    - Text files containing domains (one per line, # comments supported)

- recon/runs/
    - Immutable, timestamped historical outputs (never overwritten)

- recon/state/
    - Latest known snapshots used for diffing (overwritten each run)

## Requirements
Tools (inside Docker)
- Python 3.9+
- subfinder
- httpx

<p>The script degrades gracefully if tools are missing, but full functionality requires both.

## Roadmap Ideas
JSON state format with versioning
Nuclei execution on new live endpoints only
Per-program rate limiting
Weekly “deep scan” mode
Slack / email notification backends

## Disclaimer
Use only on targets you are authorized to test.
You are responsible for complying with program rules and laws.