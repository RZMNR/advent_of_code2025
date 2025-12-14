def create_number(x: int, y: int):
    return x * 10 + y


def get_maximum_joltage(line: str):
    max_1 = 0
    max_2 = 0
    line_length = len(line)
    for idx, i in enumerate(line):
        int_i = int(i)
        if int_i > max_1:
            if idx != line_length - 1:
                max_1 = int_i
                max_2 = 0
            else:
                max_2 = int_i
            continue

        if int_i > max_2:
            max_2 = int_i

    return create_number(max_1, max_2)


def main():
    with open("input/input.txt", "r") as file:
        joltages = []
        for line in file.readlines():
            joltages.append(get_maximum_joltage(line.rstrip("\n")))

        print(sum(joltages))


if __name__ == "__main__":
    main()
