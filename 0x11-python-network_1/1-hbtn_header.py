#!/usr/bin/python3
import sys
import urllib
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    response_id = response.headers.get("X-Request-Id")
    print(response_id)