from horus.scanners import run_subfinder, run_httpx
from horus.targets import convert_to_set, jsonl_to_dict
import paths

#TODO this doesn't work
def diff_subdomains():

    if paths.state_dir.is_dir():
        state_subdomains   = convert_to_set(paths.state_dir)

    new_subdomains     = convert_to_set(paths.run_dir)
    

    #convert old file to set, convert new file to set, compare
    if new_subdomains == state_subdomains:
        print("they are the same")
    else:
        print("different")



# load JSONL into structured data for diffing
todays_httpx     = jsonl_to_dict(f"./data/{target}/{DATE_TODAY}/httpx.json")
yesterdays_httpx = jsonl_to_dict(f"./data/{target}/{DATE_YESTERDAY}/httpx.json")

print(todays_httpx.keys())