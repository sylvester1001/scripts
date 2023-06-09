import re
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Please enter both input file and output file as a command-line argument.")
    sys.exit(1)

# get he in and output file name agruments
input_file = sys.argv[1]
output_file = sys.argv[2]
# Check if the input file exists
try:
    with open(input_file, "r") as file:
        pass
except FileNotFoundError:
    print("Input file not found.")
    sys.exit(1)

# use a set to store the unique lines that satisfy the condition
output_lines = []

# read the input file
with open(input_file, "r") as file:
    found_trigger = False

    # read the file line by line
    for line in file:
        # check if the line is the next line after "--- RULECHECK RESULTS STATISTICS"
        if found_trigger:
            # Use regular expressions to match the numbers after "width_" and before "... TOTAL"
            match = re.search(r"width_(\d+).*?(\d+)\s*\(", line)

            # If the match is successful and the second number is not 0, add the matched number to the output set
            if match and int(match.group(2)) != 0:
                extracted_number = float(match.group(1)) * 0.001
                formatted_number = "{:.3f}".format(extracted_number)
                output_lines.append(str(formatted_number) + "\n")
                # output_lines.append(match.group(1) + "\n")

        # Check if the line is "--- RULECHECK RESULTS STATISTICS"
        if line.strip() == "--- RULECHECK RESULTS STATISTICS":
            found_trigger = True

# write the unique lines to the output file
with open(output_file, "w") as file:
    file.writelines(output_lines)

print(f"Output file created to {output_file}")
