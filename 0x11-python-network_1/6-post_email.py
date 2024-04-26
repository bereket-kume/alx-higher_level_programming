#!/usr/bin/python3
"""
     Python script that takes in a URL and an email address, sends a POST request
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
