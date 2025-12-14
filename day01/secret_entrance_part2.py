DIAL_START = 50
DIAL_MIN = 0
DIAL_MAX = 99


def turn_dial_left(current_dial_position: int, clicks: int):
    dial_pos = current_dial_position
    remaining_clicks = clicks
    zero_count = 0
    while remaining_clicks > 0:
        dial_pos = 100 if dial_pos == 0 else dial_pos
        remaining_clicks -= 1
        dial_pos -= 1
        if dial_pos == 0:
            zero_count += 1

    return (zero_count, dial_pos)


def turn_dial_right(current_dial_position: int, clicks: int):
    dial_pos = current_dial_position
    remaining_clicks = clicks
    zero_count = 0
    while remaining_clicks > 0:
        dial_pos = 0 if dial_pos == 100 else dial_pos
        remaining_clicks -= 1
        dial_pos = dial_pos + 1
        if dial_pos == 100:
            zero_count += 1

    return (zero_count, dial_pos)


def main(input_path: str):
    dial_current = DIAL_START
    password = 0

    with open(input_path, "r", newline="") as file:
        for line in file:
            clicks = int(line[1:])
            direction = line[0]
            if direction == "L":
                zero_count, dial_current = turn_dial_left(dial_current, clicks)
            else:
                zero_count, dial_current = turn_dial_right(dial_current, clicks)

            password += zero_count

        print(password)


if __name__ == "__main__":
    main("input/aoc_day1_secret_entrance.txt")
    # main("input/sample.txt")
