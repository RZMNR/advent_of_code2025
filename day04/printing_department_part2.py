def remove_paper_rolls(diagram: list[str]):
    total_lines = len(diagram)
    result = 0
    for line_id, line in enumerate(diagram):
        line = list(line)
        previous_line = line_id - 1 if line_id > 0 else None
        next_line = line_id + 1 if line_id < total_lines - 1 else None
        line_length = len(line)

        for pos_id, pos in enumerate(line):
            prev_pos = pos_id - 1 if pos_id > 0 else None
            next_pos = pos_id + 1 if pos_id < line_length - 1 else None
            paper_count = 0

            if pos != "@":
                continue

            if prev_pos is not None and (line[prev_pos] in ("@", "x")):
                paper_count += 1

            if next_pos is not None and (line[next_pos] == "@"):
                paper_count += 1

            upper_bound = next_pos + 1 if next_pos else None

            paper_count += (
                diagram[previous_line][prev_pos:upper_bound].count("@")
                + diagram[previous_line][prev_pos:upper_bound].count("x")
                if previous_line is not None
                else 0
            )

            paper_count += (
                diagram[next_line][prev_pos:upper_bound].count("@")
                if next_line is not None
                else 0
            )

            if paper_count < 4:
                result += 1
                line[pos_id] = "x"

        if previous_line is not None:
            diagram[previous_line] = diagram[previous_line].replace("x", ".")

        diagram[line_id] = "".join(line)

        if next_line is None:
            diagram[line_id] = diagram[line_id].replace("x", ".")

    if result > 0:
        return result + remove_paper_rolls(diagram)
    return result


def main():
    with open("input/input.txt", "r") as file:
        content = [line.rstrip("\n") for line in file.readlines()]

    result = remove_paper_rolls(content)
    print(result)


if __name__ == "__main__":
    main()
