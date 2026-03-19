#!/bin/bash
mkdir -p XMFA_output
while IFS= read -r item; do
    echo "Working with clade ${item}"
    fas_dir="fixed_fas_output_v2/${item}"
    output_file="XMFA_output/${item}.xmfa"
    if [ -f "$output_file" ]; then
        :
    else
        # Get gene name
        for file in ${fas_dir}/*; do
            gene_name=$(basename "$file" .best.fas) # remove ".best.fas"
            echo "#${gene_name}" >> "$output_file"
            cat ${file} >> "$output_file"
            echo "=" >> "$output_file"
        done
    fi
done < "list.txt"

