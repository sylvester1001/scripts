#!/bin/bash
unalias -a

rule_file="rule.csv"
cell_file="cell_final.lib"

## 读取rule.csv文件中的第三列，提取cellnames
readarray -t cellnames < <(tail -n +3 "$rule_file" | cut -d ',' -f 3)
content=$(cat -n "$cell_file")

# --------------------------------------
new_content="$content"
for cellname in "${cellnames[@]}"; do
    if grep -q "$cellname" <<<"$new_content"; then
        new_content=$(sed "s/$cellname/${cellname}_mc/g" <<<"$new_content")
    fi
done

# 将修改后的内容写回到cell_final_mc.lib文件中
echo "$new_content" >cell_final_mc.lib