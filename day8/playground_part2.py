def squared_distance(box1, box2):
    return sum((x - y) ** 2 for x, y in zip(box1, box2))


with open("input/input.txt", "r") as file:
    boxes = []
    for line in file.readlines():
        x, y, z = [int(p) for p in line.rstrip("\n").split(",")]
        boxes.append((x, y, z))

pairs = []
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        distance = squared_distance(boxes[i], boxes[j])
        pairs.append(({boxes[i], boxes[j]}, distance))

pairs.sort(key=lambda x: x[1])

circuits = []
circuit = pairs[0][0]
for link in pairs:
    circuit = link[0]
    to_merge = []
    for i in range(len(circuits)):
        if not circuits[i].isdisjoint(circuit):
            to_merge.append(i)

    if len(to_merge) == 1:
        i = to_merge[0]
        circuits[i] = circuits[i].union(circuit)
        if circuits and len(circuits[0]) == 1000:
            print(list(circuit)[0][0] * list(circuit)[1][0])
            break
        continue

    if len(to_merge) == 2:
        i1 = to_merge[0]
        i2 = to_merge[1]
        circuits[i1] = circuits[i1].union(circuit)
        circuits[i1] = circuits[i1].union(circuits.pop(i2))
        continue

    circuits.append(circuit)
