#!/home/deborah/miniconda3/bin/python
# fix 
# Usage: python fix_fas_files.py [group] [core_genome_alignment_fas_files_directory] [ingroup_strains_file] [output_dir]

import sys
import os
import shutil

group_name = sys.argv[1]  # Example: ST555
fas_dir = sys.argv[2]  # Example: fixed_fas_output/ST555
ingroup = sys.argv[3]  # Example: list/ST555_ingroup
out_dir = sys.argv[4]  # Example: fixed_fas_output_v2/ST555


def fix_fas(group_name, fas_dir, ingroup_path, out_dir):
    print(f"Working on {group_name}...")
    print(f"Clade list: {ingroup_path}")
    print(f"Working with alignment files in {fas_dir}...")
    fas_files = [os.path.join(fas_dir, f) for f in os.listdir(fas_dir) if f.endswith('.fas')]  # list of fas files for the given clade (path included)

    # read ingroup strain list
    with open(ingroup, "r") as ingroup_file:
        ingroup_strains = [line.strip() for line in ingroup_file.readlines()]
    print(f"Ingroup strains: {ingroup_strains}")
    
    os.makedirs(out_dir, exist_ok=True)
    
    # read alignment fas files
    total=0
    print(f"Intial no. of genes: {len(fas_files)}")
    for file in fas_files:
        file_name = os.path.splitext(os.path.basename(file))[0]
        gene_record = {}
        with open(file, "r") as input_file:
            for line in input_file:
                if line[0] == ">":
                    # only keep strain name before the semicolon (;)
                    strain_name = line.split(";")[0][1:].rstrip('\n\r\a\t')
                    gene_record[strain_name] = ""
                else:
                    seq = line.rstrip('\n\r\a\t')
                    gene_record[strain_name] += seq

        # check for missing strains
        missing = [strain for strain in ingroup_strains if strain not in gene_record]
        if missing:
            total+=1
        else:
            output_path = os.path.join(out_dir, f"{file_name}.fas")
            shutil.copy2(file, output_path)
        
        
    print(f"Remaining genes after fixing: {len(fas_files)-total}")


fix_fas(group_name, fas_dir, ingroup, out_dir)