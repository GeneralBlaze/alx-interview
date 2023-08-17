#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_code_counts = {}

try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()

        # Split line into parts using spaces
        parts = line.split()

        # Validate parts length
        if len(parts) >= 8:
            # Extract status code
            status_code = parts[-2]
            status_code = status_code.strip('"')  # Remove surrounding double quotes

            # Update status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in (200, 301, 400, 401, 403, 404, 405, 500):
                    status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            # Process file size
            file_size_part = parts[-1]
            numeric_size = ""
            unit = ""
            for char in file_size_part:
                if char.isdigit():
                    numeric_size += char
                else:
                    unit += char
            numeric_size = int(numeric_size)
            unit = unit.lower()
            if unit == "kb":
                file_size = numeric_size * 1024  # Convert kb to bytes
            elif unit == "mb":
                file_size = numeric_size * 1024 * 1024  # Convert mb to bytes
            else:
                file_size = numeric_size  # Default to bytes

            # Update total file size
            total_size += file_size

            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print("Total file size:", total_size)
                for status_code in sorted(status_code_counts):
                    print("{}: {}".format(status_code, status_code_counts[status_code]))

except KeyboardInterrupt:
    print("Total file size:", total_size)
    for status_code in sorted(status_code_counts):
        print("{}: {}".format(status_code, status_code_counts[status_code]))
    sys.exit(0)

