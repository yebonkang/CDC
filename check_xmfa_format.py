#!/home/deborah/miniconda3/bin/python
# Check if each gene alignment has the same no. of strains 
# Usage: python check_xmfa.py [group] [core_genome_alignment_fas_files_directory] [ingroup_strains_file] 

import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

group_name = sys.argv[1]  # Example: ST555
fas_dir = sys.argv[2]  # Example: fixed_fas_output_v2/ST555
ingroup = sys.argv[3]  # Example: list/ST555


def detect_error(group_name,fas_dir, ingroup):
    print(f"Working on {group_name}...")
    print(f"Clade list: {ingroup}")
    #print(f"Working with alignment files in {fas_dir}...")
    fas_files = [os.path.join(fas_dir, f) for f in os.listdir(fas_dir) if f.endswith('.fas')]  # list of fas files for the given clade (path included)

    # read ingroup and outgroup strain lists
    with open(ingroup, "r") as ingroup_file:
        ingroup_strains = [line.strip() for line in ingroup_file.readlines()]
        #print(f"Ingroup strains: {ingroup_strains}")

    # read the alignment fas file
    for file in fas_files:
        file_name = os.path.splitext(os.path.basename(file))[0]
        with open(file, "r") as input_file:
            gene_record={}
            for line in input_file:
                if line[0] == ">":
                    # only keep strain name before the semicolon (;)
                    strain_name = line.split(";")[0][1:].rstrip('\n\r\a\t')
                    gene_record[strain_name] = ""
                else:
                    seq = line.rstrip('\n\r\a\t')
                    gene_record[strain_name] += seq
        # Check if all the records are there (is there any missing strain?)
        for strain in ingroup_strains:
            if strain not in gene_record:
                print(f"Warning: {strain} not found in gene record of {file_name}.fas")
    print("#################################################################")
detect_error(group_name,fas_dir, ingroup)

