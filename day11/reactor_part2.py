cache = {}
START = "svr"


def follow_path(current, paths, dac=False, fft=False):
    if current == "out":
        return int(dac and fft)

    key = (current, dac, fft)
    if key in cache:
        return cache[key]

    passed_dac = dac or current == "dac"
    passed_fft = fft or current == "fft"

    total = 0
    for path in paths.get(current, []):
        total += follow_path(path, paths, passed_dac, passed_fft)

    cache[key] = total

    return total


with open("input/input.txt", "r") as file:
    paths = {}
    for path in file.readlines():
        input, output = path.split(":")
        paths[input] = output.split()


number_of_paths = follow_path(START, paths)
print(number_of_paths)
