def get_ingredients_and_fresh_ranges(input_path: str):
    with open(input_path, "r") as file:
        ranges: list[tuple[int, int]] = []
        ingredients: list[int] = []
        switch_line = 0
        for line in file.readlines():
            line = line.strip()
            if len(line) == 0:
                switch_line = 1
                continue

            if not switch_line:
                split_line = line.split("-")
                start = int(split_line[0])
                end = int(split_line[1]) + 1
                ranges.append((start, end))
            else:
                ingredients.append(int(line))

    return ranges, ingredients


def main():
    ranges, ingredients = get_ingredients_and_fresh_ranges("input/input.txt")

    result = 0
    while ingredients:
        ingredient = ingredients.pop()
        for r in ranges:
            if ingredient >= r[0] and ingredient < r[1]:
                result += 1
                break

    print(result)


if __name__ == "__main__":
    main()
