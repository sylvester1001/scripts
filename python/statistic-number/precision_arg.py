# import sys
# import pandas as pd
# import numpy as np
# import re


# def analyze_continuous_numbers(input_filename, output_filename, precision):
#     # get the first column of data and convert it to a list
#     df = pd.read_csv(input_filename, header=None, skiprows=1)

#     # Modify the code to read and store numbers with specified decimal places without rounding
#     precision_regex = r"-p(\d+)"
#     match = re.search(precision_regex, precision)
#     decimal_places = int(match.group(1)) if match else 2
#     factor = 10**decimal_places
#     numbers = sorted(set(df[0].apply(lambda x: int(x * factor) / factor)))

#     group = []
#     count_per_group = []  # count the number of consecutive numbers in each group
#     total_numbers = len(numbers)

#     result = []  # List to store the result

#     for number in numbers:
#         group.append(number)
#         if not np.isclose(number + 0.01, numbers).any():
#             if len(group) != 0:
#                 count = len(group)
#                 count_str = (
#                     str(count) if count > 1 else ""
#                 )  # if there is only one number in the group, the number is not displayed
#                 percentage = (count / total_numbers) * 100
#                 if group[0] != group[-1]:
#                     result.append(
#                         [
#                             [group[0], group[-1]],
#                             f"[{count_str} numbers] [percentage: {percentage:.2f}%]",
#                         ]
#                     )  # Output the first and last number, the number and the percentage of each group
#                 else:
#                     result.append(
#                         [[group[0]], f"[percentage: {percentage:.2f}%]"]
#                     )  # display only the 1st number
#                 count_per_group.append(count)
#             group = []

#     # count the number of numbers in each set of consecutive numbers as a percentage of the total number
#     proportion_per_group = [count / total_numbers for count in count_per_group]

#     # Write the result to a new CSV file
#     df_result = pd.DataFrame(result)
#     df_result.to_csv(output_filename, index=False, header=False, sep="\t")

#     return proportion_per_group


# if __name__ == "__main__":
#     if len(sys.argv) > 3:
#         input_filename = sys.argv[1]  # input filename
#         output_filename = sys.argv[2]  # output filename
#         precision_arg = sys.argv[3]  # precision argument
#         proportions = analyze_continuous_numbers(
#             input_filename, output_filename, precision_arg
#         )
#         print(f"Output written to {output_filename}")
#     else:
#         print(
#             "Please enter input file, output file, and precision as command-line arguments."
#         )
#         print(
#             "e.g. python statitic-number.py <input file name> <output file name> -p2 (to specify 2 decimal places)"
#         )
# # ==================
import sys
import pandas as pd
import numpy as np

def analyze_continuous_numbers(input_filename, output_filename, precision):
    # get the first column of data and convert it to a list
    df = pd.read_csv(input_filename, header=None, skiprows=1)

    # Modify the code to read and store numbers with the specified precision
    # numbers = sorted(set(df[0].apply(lambda x: round(x, precision))))
    precision_value = 10 ** precision
    numbers = sorted(set(df[0].apply(lambda x: float(x * precision_value) / precision_value)))
    print(f"precison value is {precision_value}")
    print(f"precision is {precision}")
    group = []
    count_per_group = []  # count the number of consecutive numbers in each group
    total_numbers = len(numbers)

    result = []  # List to store the result

    for number in numbers:
        group.append(number)
        precision_power = 10**(-precision)
        if not np.isclose(number + precision_power, numbers).any():
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
                    result.append([[group[0]], f"[percentage: {percentage:.2f}%]"])  # display only the 1st number
                count_per_group.append(count)
            group = []

    # count the number of numbers in each set of consecutive numbers as a percentage of the total number
    proportion_per_group = [count / total_numbers for count in count_per_group]

    # Write the result to a new CSV file
    df_result = pd.DataFrame(result)
    df_result.to_csv(output_filename, index=False, header=False, sep="\t")

    return proportion_per_group

if __name__ == "__main__":
    if len(sys.argv) > 3:
        input_filename = sys.argv[1]  # input filename
        output_filename = sys.argv[2]  # output filename
        precision = float(sys.argv[3])  # precision argument
        proportions = analyze_continuous_numbers(input_filename, output_filename, precision)
        print(f"Output written to {output_filename}")
    else:
        print("Please enter input file, output file, and precision as command-line arguments.")
        print("e.g. python statitic-number.py <input file name> <output file name> -p 2")