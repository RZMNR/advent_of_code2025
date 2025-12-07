def create_number(number_list: list[int]):
    result = ""
    for i in number_list:
        result += str(i)

    return int(result)


def reset_code(code: list[int], start: int):
    for i in range(start, len(code)):
        code[i] = 0


def get_maximum_joltage(line: str):
    code = [0 for _ in range(12)]
    max_line_idx = len(line) - 13
    for idx, i in enumerate(line):
        if idx < max_line_idx:
            for jdx, j in enumerate(code):
                if int(i) > j:
                    code[jdx] = int(i)
                    reset_code(code, jdx + 1)
                    break
        else:
            remainder_of_line = len(line) - idx - 1
            start = len(code) - remainder_of_line - 1
            for jdx, j in enumerate(code):
                if jdx < start:
                    continue
                if int(i) > j:
                    code[jdx] = int(i)
                    reset_code(code, jdx + 1)
                    break

    return create_number(code)


def main():
    with open("input/input.txt", "r") as file:
        joltages = []
        for line in file.readlines():
            joltages.append(int(get_maximum_joltage(line.rstrip("\n"))))

        print(sum(joltages))


if __name__ == "__main__":
    main()
