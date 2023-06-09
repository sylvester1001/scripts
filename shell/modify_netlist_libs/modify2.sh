#!/bin/bash
unalias -a

orig_f="A_TOTAL_LVS_NCSIM_test.net"
output_f="A_TOTAL_LVS_NCSIM_REP_2.txt"

log_f="A_TOTAL_LVS_NCSIM.log"

readarray line_numbers <<<$(grep "ERROR" A_TOTAL_LVS_NCSIM.log | awk -F: '{print $NF}' | tr -d ")")
#在log文件中查找包含ERROR的行，并打印出这些行及其行号, 存入lines数组中

readarray net_lines <$orig_f

# for line_number in "${line_numbers[@]}"; do #遍历 lines中的每一个元素
#     sed -E "/^\s*${line_number}\s+/ s/X/M/" A_TOTAL_LVS_NCSIM.net >>$output_f
#     #以$line开头并且前面有零个或多个空白字符（\s*）的行，后面紧跟着一个或多个空白字符（\s+）
# done

#现在在line_numbers数组中存有带有ERROR的行号，net_lines数组中存有源文件中所有的行号。
#把在net_lines对应line_numbers的行中的X替换为M
for line_number in "${line_numbers[@]}"; do
    #遍历 line_numbers 数组中的每一个元素
    index=$((line_number - 1))

    net_line=${net_lines[$index]}
    #获取net_lines数组中第line_number行的内容，并将其存储在 net_line 变量中
    #数组index由0开始，行号从1开始，故减去1

    net_lines[$index]=$(echo $net_line | sed -E "s/X/M/")
done

echo "${net_lines[@]}" >$output_f

