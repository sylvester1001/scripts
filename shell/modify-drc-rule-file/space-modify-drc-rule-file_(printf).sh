#!/bin/bash
unalias -a
set -euo pipefail
#

function gen_cell_width_info() {
    local cell=$1
    local cell_prefix="${cell}_width"

    echo "$tag_info star_cell_000----"
    for i in $(seq $start $end); do
        new_cell="${cell_prefix}_${i}"

        width=$(printf "%.3f\n" "$(echo "scale=3; $i/1000" | bc)")

        # M1_width_0 = M1 with width == 0
        echo "$new_cell = ${cell} with width == $width"
        # M1_width_0{flatten M1_width_0}
        echo "$new_cell{flatten $new_cell}"

        # Add new loop for space
        for j in $(seq $space_start $space_end); do
            space_var="M1_width${i}_space_${j}"
            width_and_space="${cell}_w${i}s${j}"
            space_width=$(printf "%.3f\n" "$(echo "scale=3; $j/1000" | bc)")

            echo "$space_var = External ${new_cell} ${cell} == ${space_width} region"
            echo "${width_and_space} = ${space_var} outside ${cell}"
            echo "${width_and_space}{flatten ${width_and_space}}"
        done
        echo -e ""
    done
    echo "$tag_info end_cell_000----"
}

# -----
cell=$1            #cell name  eg, M1
start_end=$2       #start end  eg, 0-1000
space_start_end=$3 #space start end  eg, 0-1000
rule_file=$4       #rule file  eg, rule.txt

start=$(echo $start_end | cut -d '-' -f 1)
end=$(echo $start_end | cut -d '-' -f 2)
# precision=0.001

# Define space start and end variables
space_start=$(echo $space_start_end | cut -d '-' -f 1)
space_end=$(echo $space_start_end | cut -d '-' -f 2)

# Record start time
start_time=$(date +%s.%N)

# 1. delete old cell info
sed -i -E "/star_cell_000/,/end_cell_000/d" $rule_file

# 2. add new cell info
tag_info="// -----$cell"
gen_cell_width_info $cell >>$rule_file

# 3. check
echo "====DONE===="

# Execution time calculate
end_time=$(date +%s.%N)
execution_time=$(echo "$end_time - $start_time" | bc)
echo "Execution time: $execution_time seconds"
