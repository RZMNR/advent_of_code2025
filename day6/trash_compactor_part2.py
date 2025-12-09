def get_problems():
    with open("input/input.txt", "r") as file:
        problems: list[list[str]] = []
        for line in file.readlines():
            line = line.rstrip("\n")
            problems.append(list(line))

    return problems


def main():
    problems = get_problems()
    transpose = [
        [problems[j][i] for j in range(len(problems) - 1)]
        for i in range(len(problems[0]))
    ]
    total: int = 0

    operators = [op for op in problems[-1] if op != " "]

    operands = []
    for idx, problem in enumerate(transpose):
        x = "".join(problem)
        if x.count(" ") != len(x):
            operands.append(x)
            if idx != len(transpose) - 1:
                continue

        operator = operators.pop(0)
        full_problem = operator.join(operands)
        total += eval(full_problem)
        operands.clear()

    print(total)


if __name__ == "__main__":
    main()
