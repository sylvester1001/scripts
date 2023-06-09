import sys
import numpy as np


def gen_cell_width_info(cell, start, end, step):
    step_values = [
        (np.round(i,3), np.round(i + step,3)) for i in np.arange(float(start), float(end), float(step))
    ]
    cell_prefix = f"{cell}_width"
    output = []
    output.append(f"{tag_info} start_cell_000----")
    with open(input_file, "r") as file:
        intervals = file.readlines()

    for i, interval in enumerate(intervals, start=1):
        nums = interval.split()
        num1 = float(nums[0])
        num2 = float(nums[1])
        new_cell = f"{cell_prefix}_{i}"
        output.append(f"{new_cell} = {cell} with width >= {num1} <= {num2}")

        for j, (start_value, end_value) in enumerate(step_values, start=1):
            width_and_space = f"{cell}_w{i}s{j}"
            output.append(
                f"{width_and_space}_0 = External {new_cell} {cell} > {start_value} <= {end_value} opposite region\n"
                f"{width_and_space}_1 = {width_and_space}_0 outside {cell}\n"
                f"{width_and_space}_2 = not touch edge {width_and_space}_{i} {cell}\n"
                f"{width_and_space}_2{{flatten {width_and_space}_2}}\n"
            )
        # output.append(f"")
    output.append(f"{tag_info} end_cell_000----")
    return "\n".join(output)


cell = sys.argv[1]
start = float(sys.argv[2])
end = float(sys.argv[3])
step = float(sys.argv[4])
input_file = sys.argv[5]
output_file = sys.argv[6]

tag_info = "// -----" + cell

output = gen_cell_width_info(cell, start, end, step)

# Read origin rule file
with open(output_file, "r") as file:
    lines = file.readlines()

# Delete old cell info
# new_lines = []
# found_cell_info = False
# for line in lines:
#     if not found_cell_info and tag_info in line and "start_cell_000" in line:
#         found_cell_info = True
#     elif found_cell_info and tag_info in line and "end_cell_000" in line:
#         found_cell_info = False
#     elif not found_cell_info:
#         new_lines.append(line)
new_lines = []
found_cell_info = False
for line in lines:
    if not found_cell_info and "start_cell_000" in line:
        found_cell_info = True
    elif found_cell_info and "end_cell_000" in line:
        found_cell_info = False
    elif not found_cell_info:
        new_lines.append(line)

# Add new cell info
new_lines.append(output + "\n")

# Write the contents of the updated rules file
with open(output_file, "w") as file:
    file.writelines(new_lines)

print("====DONE====")
