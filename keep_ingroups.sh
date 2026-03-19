#!/bin/bash
while IFS= read -r line; do
    fas_dir="fas_output_unfixed/${line}"
    ingroup="list/${line}_ingroup"
    output_dir="./fixed_fas_output/${line}"
    mkdir -p "${output_dir}"
    python keep_ingroups.py "$fas_dir" "$ingroup" "$output_dir"
done < "list.txt"