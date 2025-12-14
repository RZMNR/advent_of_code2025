def get_ranges_sorted():
    with open("input/input.txt", "r") as file:
        ranges: list[tuple[int, int]] = []
        result = 0
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                break
            split_line = line.split("-")
            start = int(split_line[0])
            end = int(split_line[1])
            ranges.append((start, end))

        ranges.sort(reverse=True)

    return ranges


def main():
    ranges = get_ranges_sorted()
    result = 0

    x = ranges.pop()
    while ranges:
        y = ranges.pop()

        # non-overlaps
        if x[0] < y[0] and x[1] < y[0]:
            result += len(range(x[0], x[1] + 1))
            x = y

        # y contained by x
        elif x[0] <= y[0] and x[1] >= y[1]:
            continue
        else:
            x = (x[0], y[1])

        if not ranges:
            result += len(range(x[0], x[1] + 1))

    print(result)


if __name__ == "__main__":
    main()
