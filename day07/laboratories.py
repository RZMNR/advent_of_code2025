def main():
    with open("input/input.txt", "r") as file:
        origins: set[int] = {file.readline().find("S")}
        splits = 0
        for line in file.readlines():
            new_origins = set()
            while origins:
                origin = origins.pop()
                if line[origin] != "^":
                    if origin not in new_origins:
                        new_origins.add(origin)
                    continue
                splits += 1
                left = origin - 1
                right = origin + 1
                new_origins.add(left)
                new_origins.add(right)

            origins = new_origins

        print(splits)


if __name__ == "__main__":
    main()
