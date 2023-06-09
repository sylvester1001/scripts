import sys
import numpy as np


def gen_cell_width_info(cell, start, end, step):
    step_values = [
        (np.round(i, 3), np.round(i + step, 3))
        for i in np.arange(float(start), float(end), float(step))
    ]
    cell_prefix = f"{cell}_width"
    output = []
    output.append(f"{tag_info} start_cell_000----")

    for i, (start_value, end_value) in enumerate(step_values, start=1):
        output.append(
            f"{cell_prefix}_{i} = {cell} with width > {start_value} <={end_value}\n"
            f"{cell_prefix}_{i} {{flatten {cell_prefix}_{i}}}"
        )

    output.append(f"{tag_info} end_cell_000----")
    return "\n".join(output)


cell = sys.argv[1]
start = float(sys.argv[2])
end = float(sys.argv[3])
step = float(sys.argv[4])
output_file = sys.argv[5]


tag_info = "// -----" + cell

output = gen_cell_width_info(cell, start, end, step)

# Read origin rule file
with open(output_file, "r") as file:
    lines = file.readlines()

# Delete old cell info
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
