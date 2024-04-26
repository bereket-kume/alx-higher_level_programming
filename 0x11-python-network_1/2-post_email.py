#!/usr/bin/python3
"""
    send post request to given url with the given email
"""

import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print("Your email is:", body)
    