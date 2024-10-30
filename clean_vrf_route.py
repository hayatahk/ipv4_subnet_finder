#!/usr/bin/env python3

import re
import sys
from pathlib import Path

def extract_ip_subnets(filename):
    """Extracts IP subnets in the format 'x.x.x.x/xx' from each line in the file."""
    ip_subnets = []
    subnet_pattern = re.compile(r'\b\d{1,3}(?:\.\d{1,3}){3}/\d{1,2}\b')
    
    with open(filename, 'r') as file:
        for line in file:
            match = subnet_pattern.search(line)
            if match:
                ip_subnets.append(match.group())
    return ip_subnets

def write_to_file(ip_subnets, output_filename="proposed-pool.txt"):
    """Writes extracted IP subnets to the output file, raising an error if the file already exists."""
    output_path = Path(output_filename)
    
    if output_path.exists():
        raise FileExistsError(f"Error: '{output_filename}' already exists.")
    
    with output_path.open("w") as file:
        for subnet in ip_subnets:
            file.write(subnet + "\n")
    print(f"Output saved to '{output_filename}'.")

def main():
    if len(sys.argv) != 2:
        print("Usage: clean_vrf_route.py <input_file>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    # Extract IP subnets from the input file
    ip_subnets = extract_ip_subnets(input_filename)
    
    # Write to proposed-pool.txt
    write_to_file(ip_subnets)

if __name__ == "__main__":
    main()
