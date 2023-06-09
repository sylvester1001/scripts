#!/bin/bash
unalias -a

rule_file="rule.csv"
cell_file="cell_final.lib"

## 读取rule.csv文件中的第三列，提取cellnames
#cellnames=$(cat $rule_file | awk '{print $3}' | tail -n +3)
readarray cellnames <<<$(cat $rule_file | awk '{print $3}'| tail -n +3)
content=$(cat -n $cell_file)

# --------------------------------------
for cellname in "${cellnames[@]}"; do
    if grep -q "$cellname" <<<"$content"; then
        #content=${content//$cellname/$cellname"_mc"}
        new_content=$(sed "s/$cellname/${cellname}_mc/g") 
        
    fi
done

# 将修改后的内容写回到cell_final_mc.lib文件中
echo "$new_content" >cell_final_mc.lib
