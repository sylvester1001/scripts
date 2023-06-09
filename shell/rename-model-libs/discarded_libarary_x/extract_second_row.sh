#!/bin/bash

unalias -a

dir="/mnt/c/Users/CHJS/Desktop/bash/exercise/rename-model-libs/libarary_x_backup"
rule_file="rule.csv"

# 提取需要修改的cellname并存在cellnames数组中
cellnames=($(tail -n +3 "$rule_file" | awk '{print $3}'))
readarray cellnames <<<$(tail -n +3 "$rule_file" | awk '{print $3}')
readarray 