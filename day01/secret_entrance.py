DIAL_START = 50
DIAL_MIN = 0
DIAL_MAX = 99


def turn_dial_left(current_dial_position: int, clicks: int):
    new_dial_position = current_dial_position - clicks
    return divmod(new_dial_position, 100)


def turn_dial_right(current_dial_position: int, clicks: int):
    new_dial_position = current_dial_position + clicks
    return divmod(new_dial_position, 100)


def main(input_path: str):
    dial_current = DIAL_START
    password = 0

    with open(input_path, "r", newline="") as file:
        for line in file:
            clicks = int(line[1:])
            direction = line[0]
            if direction == "L":
                _, dial_current = turn_dial_left(dial_current, clicks)
            else:
                _, dial_current = turn_dial_right(dial_current, clicks)

            if dial_current == 0:
                password += 1

        print(password)


if __name__ == "__main__":
    main("input/aoc_day1_secret_entrance.txt")
