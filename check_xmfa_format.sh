#!/bin/bash

while IFS= read -r item; do
    fas_dir="fixed_fas_output_v2/${item}"
    ingroup="list/${item}_ingroup"
    if [ -d "$fas_dir" ]; then
        python check_xmfa_format.py ${item} ${fas_dir} ${ingroup}
    else
        echo "${fas_dir} not found. Skipping."
    fi
done < "list.txt"


