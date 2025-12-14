def find_invalid_id(start: int, end: int):
    invalid_ids: list[int] = []
    for i in range(start, end + 1):
        str_i = str(i)
        length_i = len(str_i)
        half_i = divmod(length_i, 2)[0]
        first = str_i[0:half_i]
        last = str_i[half_i:]

        if first == last:
            invalid_ids.append(i)

    return invalid_ids


def main():
    with open("input/input.txt", "r") as file:
        content = file.readline()
        invalid_ids = []
        for line in content.split(sep=","):
            id_range = line.split("-")
            start = int(id_range[0])
            end = int(id_range[1])

            invalid_ids.extend(find_invalid_id(start, end))

        print(sum(invalid_ids))


if __name__ == "__main__":
    main()
