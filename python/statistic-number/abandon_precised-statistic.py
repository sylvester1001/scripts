import sys
import pandas as pd
import numpy as np


def analyze_continuous_numbers(input_filename, output_filename):
    # get the first column of data and convert it to a list
    df = pd.read_csv(input_filename, header=None, skiprows=1)
    numbers = df[0].astype(float).tolist()
    numbers = [f"{num:.2f}" for num in numbers]
    numbers = list(set(numbers))
    numbers = [float(num) for num in numbers]
    group = []
    count_per_group = []  # count the number of consecutive numbers in each group
    total_numbers = len(numbers)

    result = []  # List to store the result

    for number in sorted(set(numbers)):
        group.append(number)
        if not np.isclose(number + 0.01, numbers).any():
            if len(group) != 0:
                count = len(group)
                count_str = str(count) if count > 1 else ""  # if there is only one number in the group, the number is not displayed
                percentage = (count / total_numbers) * 100
                if group[0] != group[-1]:
                    result.append(
                        [
                            [group[0], group[-1]],
                            f"[{count_str} numbers] [percentage: {percentage:.2f}%]",
                        ]
                    )  # Output the first and last number, the number and the percentage of each group
                else:
                    result.append(
                        [[group[0]], f"[percentage: {percentage:.2f}%]"]
                    )  # display only the 1st number
                count_per_group.append(count)
            group = []

    # count the number of numbers in each set of consecutive numbers as a percentage of the total number
    proportion_per_group = [count / total_numbers for count in count_per_group]

    # Write the result to a new CSV file
    df_result = pd.DataFrame(result)
    df_result.to_csv(output_filename, index=False, header=False, sep="\t")

    return proportion_per_group


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]  # input filename
        output_filename = sys.argv[2]  # output filename
        proportions = analyze_continuous_numbers(input_filename, output_filename)
        print(f"Output written to {output_filename}")
    else:
        print("Please provide an output filename as a command-line argument.")
