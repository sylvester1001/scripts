import re
import time
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


# 函数用于提取VPP和VSS文件名 / Function to extract filenames
def extract_name(filename):
    result = []
    with open(filename, "r") as file:
        lines = file.readlines()
    for line in lines:
        match = re.search(r"\s([^:]+):", line)
        if match:
            content = re.search(r"\s([^:]+)", line).group(1)
            if 0 <= len(result) <= 11:
                content += "(floating)"
            result.append(content)
    return result


# 函数用于提取文件内容并返回 DataFrame对象 / Function to extract file content and return DataFrame
def extract_content(file_path, columns_to_extract):
    data = pd.read_csv(
        file_path, header=None, skiprows=columns_to_extract - 1, usecols=[2]
    )
    return data


# 函数用于储存生成的图片 / Function to save figures
def save_figure(data, name, figure_dir):
    plt.figure()
    plt.plot(data.iloc[:, 0], data.iloc[:, 1:6])
    plt.legend(data.columns[1:6])
    plt.title(name)
    figure_outputfile = figure_dir / f"{name}.png"
    plt.savefig(figure_outputfile, dpi=300)
    plt.close()
    return figure_outputfile


# Extracts and processes files based on the provided arguments.
def extract_and_process_files(
    vpp_filename, vss_filename, folder_path, columns_to_extract, output_dir, figure_dir
):
    output_dir.mkdir(parents=True, exist_ok=True)
    figure_dir.mkdir(parents=True, exist_ok=True)

    x_axis = pd.Series([round(x * 0.04, 2) for x in range(-50, 51)])
    # Process VPP files
    for i, vpp_name in enumerate(vpp_filename, start=1):
        vpp_data = []

        for folder in range(1, 6):
            file_path = folder_path / str(folder) / "VPP" / f"{i}.csv"
            if file_path.exists():
                vpp_data.append(extract_content(file_path, columns_to_extract))

        vpp_concat = pd.concat(vpp_data, axis=1)
        vpp_concat.insert(0, "x", x_axis)

        column_names = [
            f"{vpp_name.split('-')[0]}",
            "IDD1",
            "IDD2",
            "IDD3",
            "IDD4",
            "IDD5",
        ]
        vpp_concat.columns = column_names

        vpp_outputfile = output_dir / f"{vpp_name}.csv"
        vpp_concat.to_csv(vpp_outputfile, index=False)

        vpp_figure_outputfile = save_figure(vpp_concat, vpp_name, figure_dir)

        print(f"File extracted:  {vpp_outputfile}")
        print(f"Figure extracted: {vpp_figure_outputfile}")
    # Process VSS files
    for j, vss_name in enumerate(vss_filename, start=1):
        vss_data = []

        for folder in range(1, 6):
            file_path = folder_path / str(folder) / "VSS" / f"{j}.csv"
            if file_path.exists():
                vss_data.append(extract_content(file_path, columns_to_extract))

        vss_concat = pd.concat(vss_data, axis=1)
        vss_concat.insert(0, "x", x_axis)

        column_names = [
            f"{vss_name.split('-')[0]}",
            "IDD1",
            "IDD2",
            "IDD3",
            "IDD4",
            "IDD5",
        ]
        vss_concat.columns = column_names

        vss_outputfile = output_dir / f"{vss_name}.csv"
        vss_concat.to_csv(vss_outputfile, index=False)

        vss_figure_outputfile = save_figure(vss_concat, vss_name, figure_dir)

        print(f"File extracted:  {vss_outputfile}")
        print(f"Figure extracted: {vss_figure_outputfile}")
    print("\n┬─┬ ノ('-'ノ) --Extraction completed--")


# 指定输入文件名,路径，和要提取的行数 / Specify the input filenames, folder path, and number of columns to extract
vpp_filename = extract_name("VPP.txt")
vss_filename = extract_name("VSS.txt")
folder_path = Path("./")
columns_to_extract = 253
output_dir = Path("./output_optimized_arg")
figure_dir = Path("./figure_optimized_arg")

start_time = time.time()  # 开始统计执行时间 / start measuring the execution time

# 用提供的参数调用该函数 / Call the function with the provided arguments
extract_and_process_files(
    vpp_filename, vss_filename, folder_path, columns_to_extract, output_dir, figure_dir
)

end_time = time.time()  # 结束执行时间统计 / Stop measuring the execution time
execution_time = end_time - start_time  # 计算执行时间 / Calculate the total execution time
print(f"(╯°Д°)╯︵ ┻━┻ --Execution time:{execution_time:.2f} seconds--")
