# Arithmetic Arranger for Freecodecamp.org Scientific Computing with Python certification
# Main objective: Arrange up to five problems into a typical stacked fashion using string manipulation

# Error Handling:
# No more than 5 problems [x]
# Operator must be a + or - [x]
# Operand should only contain digits [x]
# Operands must be no greater than 4 digits [x]

# Formatting:
# Single space between operator and the LONGEST operand [x]
# Operator must be on the same line as the second operand [x]
# Both operands will be in the same order as appears in operation [x]
# Number must be right-aligned [x]
# Four spaces between each problem [x]
# Dashes at the bottom of each problem, spanning the entire length from operator to operands [x]

# Example of proper vertical format
#   235
# +  52
# -----

# Function should accept "solve=False/True", if True solve the problem [x]

# Notes:
# For loops are not useful in this case because the user can input an unknown number of operations
# A WHILE loop deals with unknown number of iterations, might be more useful
# A key idea is to note store the answers in a list... like I did for several days.
# Focus on strings as the formatting, not lists. REMEMBER, THIS IS ABOUT "STRING" MANIPULATION

def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    # The principal variables
    # Strings, not lists
    problem_count = 0
    first_line = ''
    second_line = ''
    dashes = ''
    result_line = ''

    # While the length of problems is less than the problem count, continue loop
    # A For loop only works with a known number of iterations
    while len(problems) > problem_count:

        # Take the operations with the argument and split them into separate elements
        # first line = '25', '29', '3880', '34', '99'
        # second line = '+ 43', '- 58', '+ 12', '+ 798', '- 35'
        # Dashes
        # Solutions = '68', '-29', '3892', '832', '64'
        element = problems[problem_count].split()
        operand_1 = element[0]
        operand_2 = element[2]
        operator = element[1]

        # Checks what operands are being checked
        # print(operand_1, operand_2, operator)

        # Convert integers added together into strings
        if len(operand_1) < 5 and len(operand_2) < 5:
            if operand_1.isdigit() and operand_2.isdigit():
                if operator == '+':
                    solution = str(int(operand_1) + int(operand_2))
                elif operator == '-':
                    solution = str(int(operand_1) - int(operand_2))
                else:
                    return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers must only contain digits."
        else:
            return "Error: Numbers cannot be more than four digits."

        # Distance calculation and space padding
        max_length = max(len(operand_1), len(operand_2)) + 2
        # print('Max length:', max_length)
        space_padding = " " * 4

        # Adds blank spaces by multiplying the strings by the max length...
        # minus the length of the current operand
        # Add in the current operand (NOT THE LENGTH) plus the four blank spaces
        first_line += ' ' * (max_length - len(operand_1)) + operand_1 + space_padding
        #   25      29      3880       34      99

        second_line += operator + ' ' * (max_length - len(operand_2) - 1) + operand_2 + space_padding
        # + 43    - 58    +   12    + 798    - 35

        dashes += max_length * '-' + space_padding
        # ----    ----    ------    -----    ----

        result_line += ' ' * (max_length - len(solution)) + solution + space_padding
        #   68     -29      3892      832      64

        # Continues the while loop
        problem_count += 1

    if solve:
        print("The following questions and their answers are as follows! Also...")
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes.rstrip() \
                            + '\n' + result_line.rstrip()
    else:
        print("Please solve the following questions. Also...")
        arranged_problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + dashes.rstrip()

    print("Thank you for using the Arithmetic Arranger!")

    return arranged_problems


print(arithmetic_arranger(["25 + 43", "29 - 58", "3880 + 12", "34 + 798", "99 - 35"], solve=True))

# LEFT OVER CODE TO SHOW WHAT DIDN'T WORK
#         line_1 = f"{operand_1:>{width}}"
#         line_2 = f"{f'{operator} {operand_2}:>{width}'}"
#         line_3 = dashes
#
#         if solve == True:
#         if elements[1] == "+":
#         solution = int(operand_1) + int(operand_2)
#         elif elements[1] == "-":
#         solution = int(operand_1) - int(operand_2)
#         else:
#         solution = ""
#
#         results = f"{operand_1:>{width}}\n{operator}{operand_2:>{width}}" \
#         f"\n{dashes:>{width}}\n{solution}"
#         print(results)


# print("Sorted Elements:", sorted_elements)
# print("Length of Sorted Elements:", sorted_elements
