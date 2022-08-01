# The majority of testing will be conducted in main.py
def arithmetic_formatter(expressions, solve=False):
    expressions = ["45 + 45", "32 + 26"]
    numbers = '0123456789'

    number_1 = None
    number_2 = None
    addition = False
    subtraction = False
    operation_sign = None
    separated_list = []

    # Separates list into individual, readable elements
    for line in expressions:
        for word in line.split(' '):
            separated_list.append(word)

    print("The separated list:", separated_list)

    # Checks for addition or subtraction
    for i in separated_list:
        if i == "+":
            addition = True
        elif i == "-":
            subtraction = True

    # Sets the operator to addition
    if addition is True:
        operation_sign = "+"
    else:
        pass

    # Sets the operator to subtraction
    if subtraction is True:
        operation_sign = "-"
    else:
        pass

    print(
        f"   {number_1}\n"
        f"{operation_sign}  {number_2}\n"
        "______"
    )


print(arithmetic_formatter(["45 + 45"]))
