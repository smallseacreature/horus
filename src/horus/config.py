#Constants

from datetime import date, timedelta

#===============
# Datetime
#===============
DATE_TODAY     = date.today()
DATE_YESTERDAY = date.today() - timedelta(days=1)

#===============
# Compliance
#===============
RATE_LIMIT = 25

#===============
# Headers
#===============
bug_bounty_header = "User-Agent: HackerOne-Research"
contact_header    = "X-Contact: smallseacreature@wearehackerone.com"

#===============
# Lists
#===============
security_tools = ["httpx", "subfinder"]


