def area(p1, p2) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


with open("input/input.txt", "r") as file:
    points = []
    for line in file.readlines():
        x, y = [int(point) for point in line.rstrip("\n").split(",")]
        points.append((x, y))

points.sort(key=lambda x: x[1])

max = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        a = area(points[i], points[j])
        if a > max:
            max = a

print(max)
