#!/usr/bin/env python3

#v0.1.0

#=============================================================================#                                                                        
#     __   __     __     ______   ______   __         ______     ______       #  
#     /\ "-.\ \   /\ \   /\  ___\ /\  ___\ /\ \       /\  ___\   /\  == \     #   
#     \ \ \-.  \  \ \ \  \ \  __\ \ \  __\ \ \ \____  \ \  __\   \ \  __<     #   
#      \ \_\\"\_\  \ \_\  \ \_\    \ \_\    \ \_____\  \ \_____\  \ \_\ \_\   #   
#       \/_/ \/_/   \/_/   \/_/     \/_/     \/_____/   \/_____/   \/_/ /_/   #                                                                                                                                                        
#=============================================================================#
#    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀                  #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀                   #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀                 #    
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘                 #
#   ⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀                 #
#   ⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸                 #
#   ⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇                 #
#   ⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃                 #
#   ⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀                 #
#   ⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀                 #
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀                 #    
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀                 #                  
#   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 #                                                         #
#=============================================================================#                                                                       
                                                                          

#This script is designed for reconnasiance on BugBounty targets. 

#We want to run subfinder to discover subdomains, and then use httpx to check which ones are actually live.
#Then, we will check the difference, and alert via Discord webhook if changes are found
#This allows us to be aware of new endpoints for testing

# TODO add hackerone header, test

#imports
from __future__ import annotations
import argparse
import datetime as dt
import json
import shutil
import subprocess
import urllib.request
from pathlib import Path
from typing import Iterable, List, Set, Tuple, Optional


# ----------------------------
# UTIL FUNCS
# ----------------------------
def which(cmd: str) -> bool:

    """Checks if a command exists on your system"""

    return shutil.which(cmd) is not None

def run_cmd(cmd: List[str], timeout: int = 300) -> Tuple[int, str, str]:

    """Run command, return (rc, stdout, stderr). Never raises on nonzero rc."""

    try:
        p = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, "", f"timeout after {timeout}s: {' '.join(cmd)}"
    except Exception as e:
        return 127, "", f"error running {' '.join(cmd)}: {e}"
    
def normalize_lines(lines: Iterable[str]) -> List[str]:
    out: Set[str] = set()
    for line in lines:
        s = line.strip().replace("\r", "")
        if not s:
            continue
        if s.startswith("*."):
            s = s[2:]
        out.add(s)
    return sorted(out)

def read_targets_file(path: Path) -> List[str]:
    domains: List[str] = []
    for raw in path.read_text(errors="ignore").splitlines():
        s = raw.split("#", 1)[0].strip()
        if s:
            domains.append(s)
    return domains

def save_lines(path: Path, lines: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")

def load_snapshot(path: Path) -> List[str]:
    if not path.exists():
        return []
    return normalize_lines(path.read_text(errors="ignore").splitlines())

def diff(old: List[str], new: List[str]) -> Tuple[List[str], List[str]]:
    old_set, new_set = set(old), set(new)
    added = sorted(new_set - old_set)
    removed = sorted(old_set - new_set)
    return added, removed

def print_diff(label: str, added: List[str], removed: List[str]) -> bool:
    if not added and not removed:
        print(f"[=] No changes for {label}")
        return False

    print("\n====================")
    print(f"Diff for: {label}")
    print("====================")
    if added:
        print("[+] Added:")
        print("\n".join(added))
    if removed:
        print("[-] Removed:")
        print("\n".join(removed))
    return True

# ----------------------------
# RECON FUNCS
# ----------------------------

def enum_subdomains_subfinder(domain: str) -> List[str]:
    if not which("subfinder"):
        return []
    rc, out, err = run_cmd(["subfinder", "-silent", "-d", domain], timeout=300)
    # Even if rc != 0, we still try to use whatever came back on stdout
    return normalize_lines(out.splitlines())

def probe_httpx(hosts: List[str]) -> List[str]:
    if not hosts:
        return []
    if not which("httpx"):
        # If httpx isn't installed, degrade gracefully to hostnames
        return normalize_lines(hosts)

    # Feed host list via stdin; keep output stable & diff-friendly.
    # NOTE: Keep flags modest; more metadata = noisier diffs.
    try:
        p = subprocess.run(
            ["httpx", "-silent", "-follow-host-redirects"],
            input="\n".join(hosts) + "\n",
            text=True,
            capture_output=True,
            check=False,
            timeout=600,
        )
        return normalize_lines(p.stdout.splitlines())
    except subprocess.TimeoutExpired:
        return []
    except Exception:
        return []

# ----------------------------
# DISCORD
# ----------------------------

def notify_discord(webhook_url: str, content: str, timeout: int = 10) -> None:
    """
    Sends a message to Discord via webhook.
    Discord supports either "content" or rich embeds. We'll use "content" for simplicity.
    """
    if not webhook_url:
        return

    payload = {"content": content}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            _ = resp.read()  # consume
    except Exception as e:
        # Don't crash recon runs just because Discord fails
        print(f"[!] Discord notification failed: {e}")

# ----------------------------
# DOMAIN
# ----------------------------

def run_for_domain(domain: str, runs_dir: Path, state_dir: Path, ts: str) -> Tuple[bool, str]:
    run_dir = runs_dir / domain / ts
    run_dir.mkdir(parents=True, exist_ok=True)

    print(f"[*] Domain: {domain}")

    # 1) Subdomains
    print("[*] Enumerating subdomains (subfinder)...")
    subs = enum_subdomains_subfinder(domain)
    print(f"    -> {len(subs)} subs")

    # 2) Live HTTP(S)
    print("[*] Probing http(s) (httpx)...")
    live = probe_httpx(subs)
    print(f"    -> {len(live)} live entries")

    # 3) Save run artifacts
    save_lines(run_dir / "subdomains.txt", subs)
    save_lines(run_dir / "live_http.txt", live)

    # 4) Load previous snapshots
    prev_subs = load_snapshot(state_dir / f"{domain}.subdomains.txt")
    prev_live = load_snapshot(state_dir / f"{domain}.live_http.txt")

    # 5) Diff + report
    changed = False

    sub_added, sub_removed = diff(prev_subs, subs)
    changed |= print_diff(f"{domain} subdomains", sub_added, sub_removed)

    live_added, live_removed = diff(prev_live, live)
    changed |= print_diff(f"{domain} live_http", live_added, live_removed)

    # 6) Update state snapshots
    save_lines(state_dir / f"{domain}.subdomains.txt", subs)
    save_lines(state_dir / f"{domain}.live_http.txt", live)

    print(f"[*] Saved run: {run_dir}")

    # Build a concise message snippet for notifications
    summary_lines: List[str] = []
    if sub_added:
        summary_lines.append(f"Subdomains added ({len(sub_added)}): " + ", ".join(sub_added[:10]) + (" …" if len(sub_added) > 10 else ""))
    if sub_removed:
        summary_lines.append(f"Subdomains removed ({len(sub_removed)}): " + ", ".join(sub_removed[:10]) + (" …" if len(sub_removed) > 10 else ""))
    if live_added:
        summary_lines.append(f"Live added ({len(live_added)}): " + ", ".join(live_added[:10]) + (" …" if len(live_added) > 10 else ""))
    if live_removed:
        summary_lines.append(f"Live removed ({len(live_removed)}): " + ", ".join(live_removed[:10]) + (" …" if len(live_removed) > 10 else ""))

    summary = "\n".join(summary_lines) if summary_lines else ""
    return changed, summary

# ----------------------------
# MAIN
# ----------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="hackpack recon + diff (subfinder + httpx) + Discord webhook")
    parser.add_argument("--root", default=None, help="hackpack root (auto if omitted)")
    parser.add_argument("--discord-webhook", default=None, help="Discord webhook URL (or set DISCORD_WEBHOOK_URL)")
    parser.add_argument("--notify-on", choices=["any-change", "live-only"], default="live-only",
                        help="When to send Discord notifications (default: live-only)")
    args = parser.parse_args()

    # Infer hackpack root: .../recon/scripts/recon_diff.py -> root is ../../
    script_path = Path(__file__).resolve()
    inferred_root = script_path.parents[2]
    root = Path(args.root).resolve() if args.root else inferred_root

    targets_dir = root / "targets"
    runs_dir = root / "recon" / "runs"
    state_dir = root / "recon" / "state"

    if not targets_dir.exists():
        raise SystemExit(f"[!] Targets folder not found: {targets_dir}")

    if not which("subfinder"):
        print("[!] subfinder not found in PATH (install it in your Docker image).")
    if not which("httpx"):
        print("[!] httpx not found in PATH (install it in your Docker image).")

    ts = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    target_files = sorted(targets_dir.glob("*.txt"))
    if not target_files:
        raise SystemExit(f"[!] No targets found in {targets_dir} (add a .txt with domains)")

    webhook_url = args.discord_webhook or (shutil.os.environ.get("DISCORD_WEBHOOK_URL") or "")
    notify_mode = args.notify_on

    any_changes = False
    notif_chunks: List[str] = []

    for tf in target_files:
        domains = read_targets_file(tf)
        for domain in domains:
            changed, summary = run_for_domain(domain, runs_dir, state_dir, ts)
            any_changes |= changed

            # Notification logic:
            # - live-only: only notify when live_http had changes (we infer from summary lines containing "Live ")
            # - any-change: notify for any changes
            if changed and summary:
                if notify_mode == "any-change":
                    notif_chunks.append(f"**{domain}**\n{summary}")
                else:
                    # live-only
                    live_related = any(line.startswith("Live ") for line in summary.splitlines())
                    if live_related:
                        notif_chunks.append(f"**{domain}**\n{summary}")

            print("")

    if any_changes:
        print("[*] Changes detected.")
    else:
        print("[*] No changes detected across targets.")

    # Send one message per run (aggregated) to avoid spam
    if webhook_url and notif_chunks:
        msg = f"hackpack recon diff ({ts})\n\n" + "\n\n".join(notif_chunks)
        notify_discord(webhook_url, msg)

if __name__ == "__main__":
    main()