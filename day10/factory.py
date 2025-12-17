def to_mask(state):
    state = state.strip("[]")
    mask = 0
    for i, v in enumerate(state):
        if v == "#":
            mask |= 1 << i
    return mask


def button_mask(button):
    button = button.strip("()").split(",")
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
    to_check = [(0, presses)]
    while observed_states:
        state, presses = to_check.pop()

        if state == desired_state:
            return presses

        for b in buttons:
            new_state = state ^ b  # bitwise xor
            if new_state not in observed_states:
                observed_states.add(new_state)
                to_check.insert(0, (new_state, presses + 1))


machines = []
with open("input/input.txt", "r") as file:
    for line in file.readlines():
        items = line.split()
        ind_lights = to_mask(items[0])
        buttons = [button_mask(b) for b in items[1:-1]]
        machines.append((ind_lights, buttons))


minima = []
for machine in machines:
    minimum = find_minimum(machine[0], machine[1])
    minima.append(minimum)

print(sum(minima))
