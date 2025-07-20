import requests
import sys

# Read the file containing subdomains
subdoms = []
with open(sys.argv[2], "r") as f:
    for i in f:
        subdoms.append(i.strip())

f.close()

# Concatenate the subdomains with the actual domain

for i in subdoms:
    site = f"http://{i}.{sys.argv[1]}"
    try:
        requests.get(site)
    except requests.ConnectionError:
        # print("Error\n")
        pass
    else:
        print(f"{i} Exists")