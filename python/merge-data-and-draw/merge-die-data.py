import os
import re
import pandas as pd
import matplotlib.pyplot as plt

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


# 函数用于提取文件内容并返回 DataFrame 对象
def extract_content(file_path):
    data = pd.read_csv(
        file_path, header=None, skiprows=columns_to_extract - 1, usecols=[2]
    )
    return data


output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# --------------------------------------------------------------
# 遍历 VPP 目录
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

    # 添加列名
    vpp_concat.columns = [
        f"{vpp_name.split('-')[0]}",
        "IDD1",
        "IDD2",
        "IDD3",
        "IDD4",
        "IDD5",
    ]

    # 将连接的结果保存为 CSV 文件，使用提取出来的名字作为文件名
    vpp_outputfile_name = os.path.join(output_dir, f"{vpp_name}.csv")
    vpp_concat.to_csv(vpp_outputfile_name, index=False)
    print(f"File extracted: {vpp_outputfile_name}")
# ----------------------------------------------------------------
# 遍历 VSS 目录
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

    # 添加列名
    vss_concat.columns = [
        f"{vss_name.split('-')[0]}",
        "IDD1",
        "IDD2",
        "IDD3",
        "IDD4",
        "IDD5",
    ]
    # 将连接的结果保存为 CSV 文件，使用提取出来的名字作为文件名
    vss_outputfile_name = os.path.join(output_dir, f"{vss_name}.csv")
    vss_concat.to_csv(vss_outputfile_name, index=False)
    print(f"File extracted: {vss_outputfile_name}")

# -----------------------------------------
# 获取output目录下的所有CSV文件
# output_csv_files = [file for file in os.listdir("./output") if file.endswith(".csv")]

# # 遍历每个CSV文件
# for output_csv_file in output_csv_files:
#     # 构建文件路径
#     output_csv_path = os.path.join("./output", output_csv_file)

#     # 读取CSV文件
#     fig_data = pd.read_csv(output_csv_path)

#     # 获取横坐标和纵坐标数据
#     x = fig_data.iloc[:, 0]  # 第一列作为横坐标
#     y = fig_data.iloc[:, 1:6]  # 第二至第六列作为纵坐标

#     # 制图
#     plt.plot(x, y)
#     plt.legend(fig_data.columns[1:6])  # 使用列名作为图例

#     output_fig_path = "./fig"
#     os.makedirs(output_fig_path, exist_ok=True)
#     # 保存图像
#     output_csv_filename = os.path.splitext(output_csv_file)[0]  # 获取文件名（去除扩展名）
#     fig_save_name = os.path.join(output_fig_path, f"{output_csv_filename}.png")  # 保存路径
#     plt.savefig(fig_save_name)

#     # 显示图形
#     plt.show()

# 获取output目录下的所有CSV文件
output_csv_files = [file for file in os.listdir("./output") if file.endswith(".csv")]


def plot_graph(data):
    x = data.iloc[:, 0]  # 第一列作为横坐标
    y = data.iloc[:, 1:6]  # 第二至第六列作为纵坐标

    plt.plot(x, y)
    plt.legend(data.columns[1:6])  # 使用列名作为图例

    output_fig_path = "./fig"
    os.makedirs(output_fig_path, exist_ok=True)

    output_csv_filename = os.path.splitext(output_csv_file)[0]  # 获取文件名（去除扩展名）
    fig_save_name = os.path.join(output_fig_path, f"{output_csv_filename}.png")  # 保存路径
    plt.savefig(fig_save_name)

    plt.show()


# 在循环中调用画图函数
for output_csv_file in output_csv_files:
    output_csv_path = os.path.join("./output", output_csv_file)
    data = pd.read_csv(output_csv_path)
    plot_graph(data)
