#!/home/deborah/miniconda3/bin/python
#Input: em.txt file from the clonalframeML output
#Usage: python calculate_rm.py [group] [em.txt file]


import sys 
import os

group_name=sys.argv[1]  # Example: novel_76
input_path=sys.argv[2]  # Example: clonalframeml_output/novel_76.em.txt

def calculate_rm_ration(group_name, input_path):
    # Read the em.txt file
    with open(input_path, "r") as infile:
        lines = infile.readlines()
        result = {}
        for line in lines[1:]:  # Skip the header line
            parts = line.split()
            param_name = parts[0] # corresponding key from the result
            posterior_mean = float(parts[1]) # value
            result[param_name] = posterior_mean
    # Exract the parameters
    R_theta = result["R/theta"]
    invdelta = result["1/delta"]
    nu = result["nu"]
    r_m = R_theta * (1 / invdelta) * nu
    R_theta=round(R_theta, 2)
    delta=round(1 / invdelta, 2)
    nu=round(nu, 2)
    r_m=round(r_m, 2)
    return (R_theta, delta,nu, r_m)
    

record = calculate_rm_ration(group_name, input_path)
print(f"R/theta for {group_name}: {record[0]}")
print(f"delta for {group_name}: {record[1]}")
print(f"nu for {group_name}: {record[2]}")
print(f"r/m ratio for {group_name}: {record[3]}")
