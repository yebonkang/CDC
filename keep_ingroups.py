#!/home/deborah/miniconda3/bin/python
# From the panaroo core genome alignment fas files, keep only the ingroup sequences
# Input: list of strains for each group & core genome alignment fas files
# Usage: python keep_ingroups.py [core_genome_alignment_fas_files_directory] [ingroup_strains_file] [output_directory]

import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

fas_dir = sys.argv[1]  # Example: fas_output_unfixed/ST8
ingroup = sys.argv[2]  # Example: list/ST8_ingroup
output_dir = sys.argv[3]  # Example: ./fixed_fas_output/ST8


def keep_ingroups(fas_dir, ingroup, output_dir):
    print(f"Clade list: {ingroup}")
    print(f"Working with alignment files in {fas_dir}...")
    fas_files = [os.path.join(fas_dir, f) for f in os.listdir(fas_dir) if f.endswith('.fas')]  # list of fas files for the given clade (path included)

    # read ingroup and outgroup strain lists
    with open(ingroup, "r") as ingroup_file:
        ingroup_strains = [line.strip() for line in ingroup_file.readlines()]
        print(f"Ingroup strains: {ingroup_strains}")

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

        # Delete outgroup sequences
        keys=list(gene_record)
        for key in keys:
            if key not in ingroup_strains:
                #print(f"Warning: {key} not found in ingroup strain lists. Removing...")
                del gene_record[key]
        
        #Write into a new file
        sequence_record = []
        for name, seq in gene_record.items():
            sequence_record.append(SeqRecord(Seq(seq), id=name, description=""))
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{file_name}.fas")
        with open(output_path, "w") as output_handle:
            SeqIO.write(sequence_record, output_handle, "fasta")

keep_ingroups(fas_dir, ingroup, output_dir)

