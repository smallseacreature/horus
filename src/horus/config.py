#Constants

from datetime import date, timedelta

DATE_TODAY = date.today()
DATE_YESTERDAY = date.today() - timedelta(days=1)

RATE_LIMIT = 25
bug_bounty_header = "User-Agent: HackerOne-Research"
contact_header = "X-Contact: smallseacreature@wearehackerone.com"
commands_to_run = ["httpx", "subfinder"]