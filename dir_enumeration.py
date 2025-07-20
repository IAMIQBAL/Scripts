import requests
import sys

# Read wordlist

f = open(sys.argv[2], "r").read()
dirs = f.splitlines()

# Enumerate

for i in dirs:
    site = f"http://{sys.argv[1]}/{i}.html"
    req = requests.get(site)

    if req.status_code == 404:
        pass
    else:
        print(f"{i} Exists")