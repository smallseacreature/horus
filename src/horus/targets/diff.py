## just stolen from horus rn


#convert old file to set, convert new file to set, compare
todays_subdomains     = convert_to_set(f"./data/{target}/{DATE_TODAY}/subdomains.txt")
yesterdays_subdomains = convert_to_set(f"./data/{target}/{DATE_YESTERDAY}/subdomains.txt")

if todays_subdomains == yesterdays_subdomains:
    print("they are the same")
else:
    print("different")



# load JSONL into structured data for diffing
todays_httpx = jsonl_to_dict(f"./data/{target}/{DATE_TODAY}/httpx.json")
yesterdays_httpx = jsonl_to_dict(f"./data/{target}/{DATE_YESTERDAY}/httpx.json")

print(todays_httpx.keys())