import requests
import sys

def download(url, fname):
    r = requests.get(url, allow_redirects=True)
    open(fname, "wb").write(r.content)

download(sys.argv[1], sys.argv[2])