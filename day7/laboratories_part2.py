def main():
    with open("input/input.txt", "r") as file:
        first_line = file.readline()
        possible_paths: list[int] = [0 for _ in range(len(first_line))]
        origin = first_line.find("S")
        possible_paths[origin] = 1
        origins: set[int] = {origin}
        for line in file.readlines():
            new_origins = set()
            while origins:
                origin = origins.pop()
                if line[origin] != "^":
                    new_origins.add(origin)
                    continue

                left = origin - 1
                right = origin + 1
                new_origins.add(left)
                new_origins.add(right)

                possible_paths[left] += possible_paths[origin]
                possible_paths[right] += possible_paths[origin]
                possible_paths[origin] = 0

            origins = new_origins

        print(sum(possible_paths))


if __name__ == "__main__":
    main()
