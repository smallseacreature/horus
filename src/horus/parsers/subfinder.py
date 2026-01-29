
def subfinder_lists_to_message(subdomains_added, subdomains_removed) -> str:
    lines: list[str] = []

    if not subdomains_added:
        lines.append(f"No subdomains added")
    else:
        for added in subdomains_added:
            lines.append(f"[+] Subdomains added {added}")

    if not subdomains_removed:
        lines.append(f"No subdomains removed")
    else:
        for removed in subdomains_added:
            lines.append(f"[-] Subdomains removed {removed}")

    return "\n".join(lines)