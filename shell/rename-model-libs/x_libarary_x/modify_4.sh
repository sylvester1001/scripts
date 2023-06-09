#!/bin/bash
unalias -a

rule_file="rule.csv"
cell_file="cell_final.lib"

## 读取rule.csv文件中的第三列，提取cellnames
cellnames=($(tail -n +3 "$rule_file" | awk '{print $3}'))

content=$(cat "$cell_file")

new_content="$content" # 初始化new_content

# --------------------------------------
for cellname in "${cellnames[@]}"; do
    if grep -q "$cellname" <<<"$content"; then
        # new_content=$(sed "s/$cellname/${cellname}_mc/g" <<<"$new_content")
        new_content=$(sed -E "s/$cellname\s*=/${cellname}_mc =/g" <<<"$new_content")
    fi
done

# 将修改后的内容写回到cell_final_mc.lib文件中
echo "$new_content" >cell_final_mc.lib
