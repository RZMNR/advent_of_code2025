def get_problems():
    with open("input/input.txt", "r") as file:
        problems: list[list[str]] = []
        for line in file.readlines():
            line = line.rstrip()
            problems.append(line.split())

    return problems


def main():
    problems = get_problems()
    transpose = [
        [problems[j][i] for j in range(len(problems))] for i in range(len(problems[0]))
    ]
    total: int = 0

    for problem in transpose:
        x = problem[-1].join(problem[:-1])
        total += eval(x)

    print(total)


if __name__ == "__main__":
    main()
