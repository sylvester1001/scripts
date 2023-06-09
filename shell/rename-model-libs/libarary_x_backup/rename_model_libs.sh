#!/bin/bash

# 定义要修改的目录
input_dir="/mnt/c/Users/CHJS/Desktop/bash/normal_excercise/rename-model-libs/libarary_x_backup"
fixed_dir="${input_dir}_fixed"
rule_file="rule.csv"

# 返回父目录创建fixed_dir
mkdir -p "$(dirname "$fixed_dir")"
# 创建输出目录
# mkdir -p "$fixed_dir"

# 提取需要修改的cellname并存在cellnames数组中
cellnames=($(tail -n +3 "$rule_file" | awk '{print $3}'))

# 定义文件名后缀变量
file_suffix="_final.lib"
# 遍历每个.lib文件
for file in "$input_dir"/*.lib; do
  # 获取文件名和扩展名
  filename=$(basename "$file")
  extension="${filename##*.}"

  # 根据文件名后缀选择要添加的后缀
  case "$filename" in
    cell"$file_suffix")
      suffix_to_add="_mc"
      ;;
    CSL"$file_suffix")
      suffix_to_add="_nfcsl"
      ;;
    NWEIB"$file_suffix")
      suffix_to_add="_nfth_hci"
      ;;
    PEQ"$file_suffix")
      suffix_to_add="_nfpeq"
      ;;
    MEQ"$file_suffix")
      suffix_to_add="_nfmeq"
      ;;
    NSA"$file_suffix")
      suffix_to_add="_nflsa"
      ;;
    PSA"$file_suffix")
      suffix_to_add="_pflsa"
      ;;
    PXIB"$file_suffix")
      suffix_to_add="_nfthp_hci"
      ;;
    PXID"$file_suffix")
      suffix_to_add="_pft_heip2"
      ;;
    *)
      suffix_to_add=""
      ;;
  esac

  for cellname in "${cellnames[@]}"; do
    sed "s/${cellname}\s*=/${cellname}${file_suffix}/g" "$file" > "$fixed_dir/${filename%.*}${file_suffix}.${extension}"
    # sed替换文件$file中，所有${cellname}后面跟着一个或多个空格+一个等号的字符串替换为${cellname}${suffix}
    #"$fixed_dir/${filename%.*}${suffix}.${extension}" 将sed处理后的结果输出到指定的文件中
    # 如果该文件不存在则创建，如果已经存在则覆盖
  done
done