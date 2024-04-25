#!/bin/bash

#
if [ -z "$1" ]; then
    echo "Usage: ./script.sh <URL>"
    exit 1
fi

response = $(curl -s -w "%{size_download}" -o /dev/null "$1")
echo "$response"