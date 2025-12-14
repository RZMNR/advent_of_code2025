def principal_period(s):
    i = (s + s).find(s, 1, -1)
    return None if i == -1 else s[:i]


def find_invalid_id(start: int, end: int):
    invalid_ids: list[int] = []
    for i in range(start, end + 1):
        str_i = str(i)
        repeat_seq = principal_period(str_i)
        if repeat_seq is None:
            continue

        len_repeat_seq = len(repeat_seq)
        len_str_i = len(str_i)

        _, r = divmod(len_str_i, len_repeat_seq)
        if r != 0:
            continue

        if str_i.replace(repeat_seq, "") == "":
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
