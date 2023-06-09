# #!/bin/bash
# unalias -a

# rule_file="rule.csv"
# cell_file="cell_final.lib"
# output_file="cell_final_mc.lib"

# # 读取rule.csv文件中的第三列，提取cellnames到一个数组中
# mapfile -t cellnames < <(awk '{print $3}' "$rule_file" | tail -n +3)
# # readarray cellnames <<<$(awk '{print $3}' rule.csv | tail -n +3)
# # 读取cell_final.lib文件的内容
# content=$(cat "$cell_file")

# # 将修改后的内容添加到new_content变量中

# for cellname in "${cellnames[@]}"; do
#     if grep -q "$cellname" <<<"$content"; then

#         new_content=$(sed "s/$cellname/${cellname}_mc/g" <<<"$content")

#     fi
# done

# # 将修改后的内容写回到cell_final_mc.lib文件中
# echo "$new_content" >$output_file
# ---------------------------

#!/bin/bash
unalias -a

rule_file="rule.csv"
cell_file="test.lib"
output_file="test_mc.lib"

## 读取rule.csv文件中的第三列，提取cellnames

cp -f $cell_file $output_file

cellnames=(dcjs dcjsws) #($(tail -n +3 "$rule_file" | awk '{print $3}'))

content=$(cat "$output_file")

new_content="$content" # 初始化new_content

# --------------------------------------
for cellname in "${cellnames[@]}"; do
    # if grep -woE "$cellname" <<<"$content"; then
    new_content=$(sed -E "s/$cellname\s*=/${cellname}_mc =/g" <<<"$new_content")
    # fi
    echo 1111

done

# 将修改后的内容写回到cell_final_mc.lib文件中
# echo "$new_content" >$output_file
