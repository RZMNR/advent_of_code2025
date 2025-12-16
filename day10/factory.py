def push_button(initial_state: tuple[int, ...], wiring: tuple[int, ...]):
    new_state = []
    for i in wiring:
        new_state[i] = initial_state[i] % 2

    return tuple(new_state)


machines = []
with open("input/sample.txt", "r") as file:
    for line in file.readlines():
        items = line.split()
        ind_lights = tuple(int(x == "#") for x in items[0][1:-1])
        buttons = tuple(button for button in x for x in items[1:-1])
        machines.append((ind_lights, buttons))


print(machines[0][0])
print(machines[0][1])

# for machine in machines:
#     size = len(machine[0])
#     indicators = tuple(map(lambda x: int(x == "#"), machine[0]))
#     buttons = machines[0]
#     tuple(0 for )
