#!/usr/bin/python3

import re
import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {}

try:
    line_count = 0

    for line in sys.stdin:
        line = line.strip()

        # Use regular expression to parse the line in the specified format
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)', line)

        if match:
            ip, status_code, file_size = match.groups()

            # Update total file size
            total_file_size += int(file_size)

            # Update status code counts
            status_code = int(status_code)
            if status_code in (200, 301, 400, 401, 403, 404, 405, 500):
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                else:
                    status_code_counts[status_code] = 1

            line_count += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print("Total file size: File size:", total_file_size)
            for code in sorted(status_code_counts.keys()):
                print("{}: {}".format(code, status_code_counts[code]))

except KeyboardInterrupt:
    # Handle CTRL + C by printing the metrics and exiting
    print("Total file size: File size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        print("{}: {}".format(code, status_code_counts[code]))
    sys.exit(0)

