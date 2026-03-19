#!/bin/bash
while IFS= read -r line; do
    item="$line"
    fas_dir="fixed_fas_output/${item}"
    ingroup="list/${line}_ingroup"
    output_dir="fixed_fas_output_v2/${item}"
    python fix_fas_files.py "$item" "$fas_dir" "$ingroup" "$output_dir"
done < "./list.txt"