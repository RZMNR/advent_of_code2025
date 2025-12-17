def push_button(state: list[int], wiring: list[int]):
    for wire in wiring:
        state[wire] = int(not state[wire])

    return state


def find_minimum(
    desired_state: list[int],
    buttons: list[list[int]],
    initial_states: list[list[int]],
    presses: int = 0,
):
    presses += 1
    new_states = []
    for state in initial_states:
        for button in buttons:
            new_state = push_button(state.copy(), button)
            if new_state == desired_state:
                return presses
            new_states.append(new_state)
    return find_minimum(desired_state, buttons, new_states, presses)


machines = []
with open("input/input.txt", "r") as file:
    for line in file.readlines():
        items = line.split()
        ind_lights = [int(x == "#") for x in items[0][1:-1]]
        buttons = [
            [int(x) for x in item.strip("()").split(",")] for item in items[1:-1]
        ]
        machines.append((ind_lights, buttons))


minima = []
for machine in machines:
    initial_state = [0 for _ in range(len(machine[0]))]
    minimum_presses = find_minimum(machine[0], machine[1], [initial_state])
    minima.append(minimum_presses)

print(sum(minima))
