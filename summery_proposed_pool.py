#!/usr/bin/env python3

import sys
from pathlib import Path
from collections import defaultdict

def process_ips(filename):
    """Processes IPs to remove duplicates based on the first two octets, 
       and counts duplicates for each unique prefix."""
    ip_dict = defaultdict(list)

    # Read the file and store IPs by their first two octets
    with open(filename, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip:
                first_two_octets = '.'.join(ip.split('.')[:2])
                ip_dict[first_two_octets].append(ip)

    # Prepare result list to write to file
    result = []
    for first_two_octets, ips in ip_dict.items():
        kept_ip = ips[0]
        duplicates_count = len(ips) - 1  # Number of duplicates
        if duplicates_count > 0:
            result.append(f"{kept_ip}  # repeated {duplicates_count} time(s)")
        else:
            result.append(kept_ip)

    return result

def write_to_file(output_filename, data):
    """Writes processed IPs to the specified output file."""
    output_path = Path(output_filename)
    
    if output_path.exists():
        output_path.unlink()  # Optional: Remove file if it already exists to overwrite

    with output_path.open("w") as file:
        for line in data:
            file.write(line + "\n")
    print(f"Output saved to '{output_filename}'.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <input_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    
    # Process IPs to remove duplicates and count repetitions
    processed_ips = process_ips(input_filename)
    
    # Write results to summery proposed-pool.txt
    write_to_file("summery-proposed-pool.txt", processed_ips)

if __name__ == "__main__":
    main()
