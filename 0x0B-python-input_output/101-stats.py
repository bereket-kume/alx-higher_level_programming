#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    parts = line.split(" ")
    if len(parts) >= 7:
        return int(parts[-2]), parts[-1].strip()
    return None, None

line_count = 0
total_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        line_count += 1
        size, code = parse_line(line)
        if size is not None and code is not None:
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
            else:
                status_codes[code] = 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
