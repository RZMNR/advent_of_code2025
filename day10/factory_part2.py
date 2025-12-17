def to_mask(joltages):
    joltages = joltages.strip("{}").split(",")
    mask_list = [int(x) % 2 for x in joltages]
    mask = 0
    for i, v in enumerate(mask_list):
        mask |= 1 << i
    return mask


def button_mask(button):
    button = button.strip("()").split(",")
    mask = 0
    for i in button:
        mask ^= 1 << int(i)
    return mask


def find_buttons_pressed(
    desired_state: int,
    buttons: list[int],
):
    observed_states = {0}
    to_check = [(0, [])]
    while observed_states:
        state, buttons_pressed = to_check.pop()

        if state == desired_state:
            return buttons_pressed

        for b in buttons:
            new_state = state ^ b  # bitwise xor
            if new_state not in observed_states:
                observed_states.add(new_state)
                buttons_pressed.append(b)
                to_check.insert(0, (new_state, buttons_pressed))


machines = []
with open("input/sample.txt", "r") as file:
    for line in file.readlines():
        items = line.split()
        buttons = [button_mask(b) for b in items[1:-1]]
        joltages = items[-1]
        machines.append((buttons, joltages))

for machine in machines:
    buttons_pressed = find_buttons_pressed(to_mask(joltages), machine[0])
    print(buttons_pressed)
