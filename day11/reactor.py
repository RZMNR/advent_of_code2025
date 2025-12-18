def follow_path(all_paths, possible_paths, n=0):
    if "out" in possible_paths:
        return 1
    for path in possible_paths:
        n += follow_path(all_paths, all_paths[path])

    return n


with open("input/input.txt", "r") as file:
    paths = {}
    for path in file.readlines():
        input, output = path.split(":")
        paths[input] = output.split()


start = paths["you"]
number_of_paths = follow_path(paths, start)
print(number_of_paths)
