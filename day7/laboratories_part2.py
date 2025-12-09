def main():
    with open("input/sample.txt", "r") as file:
        contents = file.readlines()
    rows = len(contents)
    columns = len(contents[0])

    table = [[0] * columns for _ in range(rows)]

    origin = contents[0].find("S")
    table[0][origin] = 1

    for row in range(1, rows):
        for col in range(columns):
            if contents[row][col] == "^":
                table[row][col] += table[row - 1][col - 1]
                table[row][col] += table[row - 1][col + 1]
            else:
                table[row][col] += table[row - 1][col]

    print(sum(table[rows - 1]))


if __name__ == "__main__":
    main()
