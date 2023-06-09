import os

lib_names = {"tt": [], "ff": [], "fs": [], "sf": []}

# 文件读取顺序
file_order = [
    "NF_model.lib",
    "NFL_model.lib",
    "PF_model.lib",
    "PFL_model.lib",
    "nflsa_model.lib",
    "nfpeq_model.lib",
    "nfmeq_model.lib",
    "pflsa_model.lib",
    "NFT_model.lib",
    "NFLT_model.lib",
    "nft_hci_model.lib",
    "PFT_model.lib",
    "PFLT_model.lib",
    "pft_heip_model.lib",
    "nfth_hci_model.lib",
    "nfthp_hci_model.lib",
    "pft_heip2_model.lib",
    "mc_model.lib",
    "diode.lib",
    "resistor.lib",
]

for filename in file_order:
    if filename.endswith(".lib"):
        with open(filename, "r") as file:
            lines = file.readlines()

        current_lib_name = None  # 存储当前lib_name
        current_lib_content = []  # 存储当前lib_name对应的内容

        for line in lines:  # 遍历每行内容
            line = line.strip()

            # 提取lib_name
            if line.startswith(".lib"):  # 以.lib开始，开始提取
                lib_name = line.split(".lib")[1].strip().lower()

                lib_name = (  # 处理dio_和res_开始的lib_name
                    lib_name[4:]  # 去掉以'dio_' and 'res_'开头的lib_name的前四个字符
                    if lib_name.startswith("dio_") or lib_name.startswith("res_")
                    else lib_name
                )

                # 如果lib_name存在于字典中，则将current_lib_name设为当前lib_name，且重置current_lib_content为空，以存储该段落
                if lib_name in lib_names:
                    current_lib_name = lib_name
                    current_lib_content = []
                continue

            if line.startswith(".param"):  # 忽略.param行
                continue

            if line.startswith(".endl"):  # 一段结束，将当前lib_name段添加到相应的lib_names中
                if current_lib_name is not None:  # 检查是否不为空，是则表示一个完整的段落结束
                    # 将其添加到字典中current_lib_name键对应的列表中
                    lib_names[current_lib_name].append(current_lib_content)
                    current_lib_name = None
                    current_lib_content = []
                continue

            # 提取数据行
            cell_data = line.split("=")[0].strip()
            current_lib_content.append(line)  # 将整行内容添加到current_lib_content中

# 将结果写入输出文件whole.lib
with open("./output/all_model.lib", "w") as output_file:
    for key, values in lib_names.items():
        output_file.write(f".lib {key}\n.param\n")
        # output_file.write(".param\n")
        for value in values:
            for cell_data in value:
                output_file.write(f"{cell_data}\n")
        output_file.write(f'\n.lib "./all_model.lib" core\n' + f".endl {key}\n\n")
        # output_file.write(f".endl {key}\n\n")

print(
    """
=================
| O . J . B . K |
=================
"""
)