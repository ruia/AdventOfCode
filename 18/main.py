import numpy as np
import scipy.ndimage as ndi

def part_one(input_file):
    cubes = []
    n_exposed = 0

    with open(input_file) as f:
        for line in f:
            cubes.append(eval(line.strip()))
    
    for x, y, z in cubes:
        for dx, dy, dz in (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ):

            if (x + dx, y + dy, z + dz) not in cubes:
                n_exposed += 1

    return n_exposed

def part_two(input_file):
    n_exposed = 0

    with open(input_file) as f:
        s = f.read()
        cubes = np.array([[int(val) for val in line.split(',')] for line in s.splitlines()])

    space = np.zeros(cubes.max(axis=0) + 1)

    i, j, k = cubes.T
    space[i, j, k] = 1

    space = ndi.binary_fill_holes(space)

    cubes = set(zip(*np.where(space)))

    for x, y, z in cubes:
        for dx, dy, dz in (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ):

            if (x + dx, y + dy, z + dz) not in cubes:
                n_exposed += 1

    return n_exposed

def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 64
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    assert part_two(test) == 58
    print(f"Total part 2 test: {part_two(test)}")
    print(f"Total part 2 input: {part_two(input)}")


if __name__ == '__main__':
    main()