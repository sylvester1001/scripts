import os
import re
import pandas as pd
import matplotlib.pyplot as plt

# 定义输出目录
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)
figure_dir = "./figure"
os.makedirs(figure_dir, exist_ok=True)

# 定义目录和提取列数
folder_path = "./"
columns_to_extract = 253

# 生成第一列x坐标
x_axis = pd.Series([round(x * 0.04, 2) for x in range(-50, 51)])


# 提取VSS和VPP文件名
def extract_name(filename):
    result = []
    with open(filename, "r") as file:
        lines = file.readlines()
    for line in lines:
        match = re.search(r"\s([^:]+):", line)
        if match:
            content = re.search(r"\s([^:]+)", line).group(1)
            if 0 <= len(result) <= 11:  # 1-12行提取第一个空格和第一个冒号间的内容，并加上(floating)
                content += "(floating)"
            result.append(content)
    return result


vpp_filename = extract_name("VPP.txt")
print(vpp_filename)
vss_filename = extract_name("VSS.txt")


# 函数用于提取文件内容并返回 DataFrame对象
def extract_content(file_path):
    data = pd.read_csv(
        file_path, header=None, skiprows=columns_to_extract - 1, usecols=[2]
    )
    return data


# 遍历 VPP 目录 --------------------------------------------------------------
for i, vpp_name in enumerate(vpp_filename, start=1):
    vpp_data = []  # 用于存储每个 VPP 文件的内容

    # 遍历文件夹 1 到 5
    for folder in range(1, 6):
        file_path = os.path.join(folder_path, str(folder), "VPP", f"{i}.csv")
        if os.path.exists(file_path):
            vpp_data.append(extract_content(file_path))

    # 将提取的内容按列连接
    vpp_concat = pd.concat(vpp_data, axis=1)
    vpp_concat.insert(0, "x", x_axis)  # 添加坐标列

    # 添加列名，VSS和VPP列名相同
    column_names = [f"{vpp_name.split('-')[0]}", "IDD1", "IDD2", "IDD3", "IDD4", "IDD5"]
    vpp_concat.columns = column_names

    # 将连接的结果保存为 CSV 文件，使用提取出来的名字作为文件名
    vpp_outputfile_name = os.path.join(output_dir, f"{vpp_name}.csv")
    vpp_concat.to_csv(vpp_outputfile_name, index=False)

    # 制图 -----------------------------------------------------------------
    plt.figure()
    plt.plot(vpp_concat.iloc[:, 0], vpp_concat.iloc[:, 1:6])
    plt.legend(vpp_concat.columns[1:6])
    # plt.xlabel("x")
    # plt.ylabel("IDD")
    plt.title(vpp_name)
    vpp_figure_outputfile_name = os.path.join(figure_dir, f"{vpp_name}.png")
    plt.savefig(vpp_figure_outputfile_name, dpi=300)
    plt.close()
    print(
        f"File extracted:  {vpp_outputfile_name}\nFigure extracted:{vpp_figure_outputfile_name}"
    )

# 遍历 VSS 目录 --------------------------------------------------------------
for j, vss_name in enumerate(vss_filename, start=1):
    vss_data = []  # 用于存储每个 VSS 文件的内容

    # 遍历文件夹 1 到 5
    for folder in range(1, 6):
        file_path = os.path.join(folder_path, str(folder), "VSS", f"{j}.csv")
        if os.path.exists(file_path):
            vss_data.append(extract_content(file_path))

    # 将提取的内容按列连接
    vss_concat = pd.concat(vss_data, axis=1)
    vss_concat.insert(0, "x", x_axis)  # 添加坐标列

    # 添加列名，VSS和VPP列名相同
    column_names = [f"{vss_name.split('-')[0]}", "IDD1", "IDD2", "IDD3", "IDD4", "IDD5"]
    vss_concat.columns = column_names

    # 将连接的结果保存为 CSV 文件，使用提取出来的名字作为文件名
    vss_outputfile_name = os.path.join(output_dir, f"{vss_name}.csv")
    vss_concat.to_csv(vss_outputfile_name, index=False)

    # 制图 -------------------------------------------------------------------
    plt.figure()
    plt.plot(vss_concat.iloc[:, 0], vss_concat.iloc[:, 1:6])
    plt.legend(vss_concat.columns[1:6])
    # plt.xlabel("x")
    # plt.ylabel("IDD")
    plt.title(vss_name)
    vss_figure_outputfile_name = os.path.join(figure_dir, f"{vss_name}.png")
    plt.savefig(vss_figure_outputfile_name, dpi=300)
    plt.close()
    print(
        f"File extracted:  {vss_outputfile_name}\nFigure extracted:{vss_figure_outputfile_name}" #提示提取结束和提取结果
    )
print("--Extraction completed--")
