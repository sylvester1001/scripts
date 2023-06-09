import sys
import time


def gen_cell_width_info(cell, start, end, space_start, space_end):
    cell_prefix = f"{cell}_width"
    output = []
    output.append(f"{tag_info} start_cell_000----")
    count = 0
    for i in range(start, end + 1):
        new_cell = f"{cell_prefix}_{i}"
        width = round(i / 1000, 3)

        # M1_width_0 = M1 with width == 0
        output.append(f"{new_cell} = {cell} with width == {width}")
        # M1_width_0{flatten M1_width_0}
        output.append(f"{new_cell}{{flatten {new_cell}}}")

        # Add new loop for space
        for j in range(space_start, space_end + 1):
            space_var = f"{cell}_width{i}_space_{j}"
            width_and_space = f"{cell}_w{i}s{j}"
            space_width = round(j / 1000, 3)

            output.append(
                f"{space_var} = External {new_cell} {cell} == {space_width} region"
            )
            output.append(f"{width_and_space} = {space_var} outside {cell}")
            output.append(f"{width_and_space}{{flatten {width_and_space}}}")

        output.append("")
        count += 1

        if count % 100 == 0:
            print(f"{count} times completed")

    output.append(f"{tag_info} end_cell_000----")
    return "\n".join(output)


cell = sys.argv[1]
start_end = sys.argv[2]
space_start_end = sys.argv[3]
rule_file = sys.argv[4]

start, end = map(int, start_end.split("-"))
space_start, space_end = map(int, space_start_end.split("-"))

tag_info = "// -----" + cell

start_time = time.time()  # Timer start

output = gen_cell_width_info(cell, start, end, space_start, space_end)

# Read origin rule file
with open(rule_file, "r") as file:
    lines = file.readlines()

# Delete old cell info
new_lines = []
found_cell_info = False
for line in lines:
    if not found_cell_info and tag_info in line and "start_cell_000" in line:
        found_cell_info = True
    elif found_cell_info and tag_info in line and "end_cell_000" in line:
        found_cell_info = False
    elif not found_cell_info:
        new_lines.append(line)

# Add new cell info
new_lines.append(output + "\n")

# Write the contents of the updated rules file
with open(rule_file, "w") as file:
    file.writelines(new_lines)

# Timer end
end_time = time.time()
execution_time = end_time - start_time

print("====DONE====")
print(f"Execution time: {execution_time} seconds")
