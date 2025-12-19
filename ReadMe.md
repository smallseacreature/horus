hackpack-recon
A Docker-first reconnaissance and change-detection pipeline for bug bounty and security research.
This tool runs passive subdomain enumeration, probes live HTTP(S) services, stores historical snapshots, diffs results between runs, and sends Discord alerts only when meaningful changes occur.

Designed to run unattended in a homelab using Docker + cron/systemd.

Features
Passive subdomain enumeration using subfinder
Live HTTP(S) probing using httpx
Timestamped historical runs
Stable state snapshots for reliable diffs
Added / removed detection (no noisy reordering diffs)
Optional Discord webhook notifications
Safe for automation (no shell execution, fail-soft behavior)
Docker-first (host stays clean)
Project Structure
hackpack/
├── targets/
│   └── example.txt
├── recon/
│   ├── scripts/
│   │   └── recon_diff.py
│   ├── runs/
│   │   └── <domain>/<timestamp>/
│   │       ├── subdomains.txt
│   │       └── live_http.txt
│   └── state/
│       ├── <domain>.subdomains.txt
│       └── <domain>.live_http.txt
├── Dockerfile
└── docker-compose.yml
Key directories
targets/
Text files containing domains (one per line, # comments supported)
recon/runs/
Immutable, timestamped historical outputs (never overwritten)
recon/state/
Latest known snapshots used for diffing (overwritten each run)
Requirements
Tools (inside Docker)
Python 3.9+
subfinder
httpx
The script degrades gracefully if tools are missing, but full functionality requires both.
Installation (Docker)
1. Clone or copy into your homelab
mkdir -p /opt/hackpack
cd /opt/hackpack
Place:
recon/scripts/recon_diff.py
Dockerfile
docker-compose.yml
2. Add targets
Create a file like:
targets/example.txt
Example:
example.com
test.com
# staging.example.org
3. Build the Docker image
docker compose build
4. Run manually (test)
docker compose run --rm recon
You should see:
subdomain counts
live endpoint counts
diff output (if changes exist)
new folders under recon/runs/
Discord Notifications
Create a webhook
Discord server → channel settings → Integrations → Webhooks
Copy the webhook URL
Pass the webhook to the script
Option A: CLI argument
docker compose run --rm recon \
  python3 recon/scripts/recon_diff.py \
  --discord-webhook https://discord.com/api/webhooks/...
Option B: Environment variable (recommended)
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
docker compose run --rm recon
Notification modes
--notify-on live-only   # default (only new/removed live URLs)
--notify-on any-change  # subdomains OR live URLs
Automation
Cron (host-based, recommended)
Run every 6 hours:
0 */6 * * * cd /opt/hackpack && /usr/bin/docker compose run --rm recon >> recon/recon.log 2>&1
Optional: prevent overlapping runs
0 */6 * * * /usr/bin/flock -n /tmp/hackpack-recon.lock \
  -c "cd /opt/hackpack && /usr/bin/docker compose run --rm recon" \
  >> recon/recon.log 2>&1
systemd timer (best long-term)
Use a oneshot service that runs:
docker compose run --rm recon
(Recommended if your homelab runs 24/7.)
How It Works (High-Level)
Read domains from targets/*.txt
Enumerate subdomains with subfinder
Probe live HTTP(S) services with httpx
Save results to a timestamped run directory
Diff against previous state snapshots
Print added/removed results
Update snapshots
Send a single aggregated Discord alert if configured
Design Principles
Fail-soft, not fail-fast
Partial results are better than no results in recon.
Stable diffs
Normalization removes noise (ordering, duplicates, wildcards).
No shell execution
Prevents injection and environment-specific bugs.
Separation of concerns
Enumeration, probing, diffing, and notification are isolated.
Versioning
This project follows semantic versioning in 0.x.y until the state format stabilizes.
0.x.0 → features or breaking changes
0.x.y → fixes only
Roadmap Ideas
JSON state format with versioning
Nuclei execution on new live endpoints only
Per-program rate limiting
Weekly “deep scan” mode
Slack / email notification backends
Disclaimer
Use only on targets you are authorized to test.
You are responsible for complying with program rules and laws.
If you want, next I can:
add a CHANGELOG.md
embed version metadata into the script + Docker image
write a SECURITY.md
or refactor this into a multi-container recon stack




ChatGPT can make mistakes. Check important info.