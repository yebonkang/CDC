#!/bin/bash

item=$1
input_file="clonalframeml_output/${item}.em.txt"

python calculate_rm.py ${item} ${input_file}