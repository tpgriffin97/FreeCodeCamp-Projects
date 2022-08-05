def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    sorted_elements = []
    operand_1 = ""
    operand_2 = ""

    for problem in problems:
        elements = problem.split(" ")
        print("Elements:", elements)
        sorted_elements.append(elements)

        if not elements[0].isdigit() or not elements[2].isdigit():
            return "Error: Numbers must only contain digits."
        elif elements[0].isdigit() and elements[2].isdigit():
            if len(elements[0]) > 4 or 4 < len(elements[2]):
                return "Error: Numbers cannot be more than four digits."
            else:
                operand_1 = elements[0]
                operand_2 = elements[2]

        if elements[1] not in "-+":
            return "Error: Operator must be '+' or '-'"
        elif elements[1] in "-+":
            operator = elements[1]

        max_length = max(len(elements[0]), len(elements[2]))
        width = max_length + 2
        dashes = "-" * width
        # print(sorted_elements)

        # print(operand_1)
        # print(operand_2)

        line_1 = f"{operand_1:>{width}}"
        line_2 = f"{operator} {operand_2}:>{width}"
        line_3 = dashes

        if solve == True:
            if elements[1] == "+":
                solution = int(operand_1) + int(operand_2)
            elif elements[1] == "-":
                solution = int(operand_1) - int(operand_2)
        else:
            solution = ""

        results = f"{operand_1:>{width}}\n{operator}{operand_2:>{width}}" \
                  f"\n{dashes:>{width}}\n{solution}"
        print(results)


# print("Sorted Elements:", sorted_elements)
# print("Length of Sorted Elements:", sorted_elements

print(arithmetic_arranger(["25 + 43", "29 - 58", "3880 + 12", "34 + 798", "99 - 35"], solve=False))
