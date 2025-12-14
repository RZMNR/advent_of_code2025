def area(p1, p2) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def crosses_edge(edge, min_x, max_x, min_y, max_y):
    (x1, y1), (x2, y2) = edge

    if x1 == x2:
        return min_x < x1 < max_x and y2 > min_y and y1 < max_y
    else:
        return min_y < y1 < max_y and x2 > min_x and x1 < max_x


def is_valid(p1, p2, edges):
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])

    for edge in edges:
        if crosses_edge(edge, min_x, max_x, min_y, max_y):
            return False
    return True


with open("input/input.txt", "r") as file:
    red_tiles = [
        tuple(map(int, line.rstrip("\n").split(","))) for line in file.readlines()
    ]

edges = [
    ((min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2)))
    for (x1, y1), (x2, y2) in zip(red_tiles, red_tiles[1:] + red_tiles[:1])
]

max_area = 0
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        a = area(red_tiles[i], red_tiles[j])
        if a <= max_area:
            continue
        if is_valid(red_tiles[i], red_tiles[j], edges):
            max_area = a


print(max_area)
