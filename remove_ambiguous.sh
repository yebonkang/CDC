#!/bin/bash
mkdir -p XMFA_output_v2
while IFS= read -r item; do
    XMFA_path="XMFA_output/${item}.xmfa"
    output_path="XMFA_output_v2/${item}.xmfa"
    sed '/^[#>]/! s/N/-/g' ${XMFA_path} > ${output_path}
done < "./list.txt"