#/bin/bash
# script that takes url and send request
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r'
