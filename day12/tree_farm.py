with open("input/input.txt", "r") as file:
    area_of_shapes = {}
    idx = 0
    valid_regions = 0

    for line in file.readlines():
        line = line.rstrip()
        if line.endswith(":"):
            idx = int(line[:-1])
            area_of_shapes[idx] = 0

        elif "#" in line:
            area_of_shapes[idx] += line.count("#")

        elif "x" in line:
            dimensions, counts = line.split(":")
            width, height = map(int, dimensions.split("x"))
            counts = map(int, counts.split())

            area_of_presents = sum(
                [count * area_of_shapes[i] for i, count in enumerate(counts)]
            )

            if area_of_presents <= width * height:
                valid_regions += 1

print(valid_regions)
