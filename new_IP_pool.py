#!/usr/bin/env python3

import sys
from pathlib import Path

def read_ip_file(filename):
    """Reads a file and returns a dictionary with the first two octets as keys and full IPs as values."""
    ip_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip:
                first_two_octets = '.'.join(ip.split('.')[:2])
                if first_two_octets not in ip_dict:
                    ip_dict[first_two_octets] = []
                ip_dict[first_two_octets].append(ip)
    return ip_dict

def find_no_overlap(proposed_ips, existing_octets):
    """Finds IPs in proposed-pool that do not overlap with existing-pool based on first two octets."""
    no_overlap_ips = []
    for first_two_octets, ips in proposed_ips.items():
        if first_two_octets not in existing_octets:
            no_overlap_ips.extend(ips)
    return no_overlap_ips

def find_overlap(proposed_ips, existing_octets):
    """Finds IPs in proposed-pool that overlap with existing-pool based on first two octets."""
    overlap_ips = []
    for first_two_octets, ips in proposed_ips.items():
        if first_two_octets in existing_octets:
            overlap_ips.extend(ips)
    return overlap_ips

def write_to_file(output_filename, data):
    """Writes data to the specified file, raising an error if the file already exists."""
    output_path = Path(output_filename)
    if output_path.exists():
        raise FileExistsError(f"Error: '{output_filename}' already exists.")
    
    with output_path.open("w") as file:
        for ip in data:
            file.write(ip + "\n")
    print(f"Output saved to '{output_filename}'.")

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ['nooverlap', 'overlap']:
        print("Usage: python3 new_IP_pool.py <nooverlap|overlap>")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    # Read and process the IPs from both files
    proposed_ips = read_ip_file('proposed-pool.txt')
    existing_ips = read_ip_file('existing-pool.txt')
    
    # Create a set of the first two octets from existing IPs
    existing_octets = set(existing_ips.keys())
    
    # Perform the operation based on the mode
    if mode == 'nooverlap':
        no_overlap_ips = find_no_overlap(proposed_ips, existing_octets)
        output_filename = "no-overlap-proposed-pool.txt"
        write_to_file(output_filename, no_overlap_ips)
    elif mode == 'overlap':
        overlap_ips = find_overlap(proposed_ips, existing_octets)
        output_filename = "overlapped-subnets.txt"
        write_to_file(output_filename, overlap_ips)

if __name__ == "__main__":
    main()
