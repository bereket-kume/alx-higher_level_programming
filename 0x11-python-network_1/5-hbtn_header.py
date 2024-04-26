#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL
"""
import sys
import requests

url = sys.argv[1]
response = requests.get(url)
print(response.headers.get('X-Request-Id'))
