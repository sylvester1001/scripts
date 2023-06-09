#! /bin/bash

unalias -a

input_file="output.vec.bk"
output_file="output.vec.bk_fixed"

content=$(cat $input_file)

#new_content=$(echo "$content" | sed -E -e 's/tb\.IA_TOTAL_LVS_NCSIM\.//' -e 's/net016/net016_dy/' -e 's/net017/net017_dy/' -e 's/\[/\</; s/\]/\>/')

#匹配以tb.I开头，[^.]* 表示0个或多个不是.的字符，以.结尾的字符串，替换为空
new_content=$(echo "$content" | sed -E \
    -e 's/tb\.I[^\.]*\.//' \
    -e 's/net016/net016_dy/' \
    -e 's/net017/net017_dy/' \
    -e 's/\[/\</; s/\]/\>/')

#new_content=$(echo "$content" | grep "tb.IA_TOTAL_LVS_NCSIM." | tr -d "tb.IA_TOTAL_LVS_NCSIM." | sed 's/net016/net016_dy/' -e 's/net017/net017_dy/' -e 's/\[/\</; s/\]/\>/')
old_content=$(echo "$content" | sed -E \
    -e)

echo "$new_content" >$output_file
