def to_mask(state):
    mask = 0
    for i, v in enumerate(state):
        if v % 2 == 0:
            mask |= 1 << i
    return mask


def button_mask(button):
    mask = 0
    for i in button:
        mask ^= 1 << int(i)
    return mask


def find_minimum(
    desired_state: int,
    buttons: list[int],
):
    observed_states = {0}
    presses = 0
    to_check = [(0, presses, [])]
    while to_check:
        state, presses, buttons_pressed = to_check.pop()

        if state == desired_state:
            return (presses, buttons_pressed)

        for b in buttons:
            new_state = state ^ button_mask(b)  # bitwise xor
            if new_state not in observed_states:
                observed_states.add(new_state)
                new_buttons = buttons_pressed.copy()
                new_buttons.append(b)
                to_check.insert(0, (new_state, presses + 1, new_buttons))


machines = []
with open("input/sample.txt", "r") as file:
    for line in file.readlines():
        items = line.split()
        buttons = [list(map(int, b.strip("()").split(","))) for b in items[1:-1]]
        joltages = [int(i) for i in items[-1].strip("{}").split(",")]
        machines.append((buttons, joltages))


minima = []
for machine in machines:
    minimum, btns = find_minimum(to_mask(machine[1]), machine[0])
    minima.append(minimum)
    print(btns)

print(sum(minima))
