from math import ceil

def part_one(input_file):
    sum_signal_strengths = 0
    cycles = [20, 60, 100, 140, 180, 220]

    with open(input_file) as f:
        instructions = []
        for line in f:
            line = line.strip().split(' ')
            instruction = line[0]
            if (len(line) > 1):
                value = line[1]

            instructions.append(line)

        x = 1
        cycle = 0

        while(len(instructions) > 0):
            cycle += 1
            if (cycle in cycles):
                sum_signal_strengths += (cycle * x)      

            line = instructions.pop(0)
            instruction = line[0]
            if (len(line) > 1):
                value = int(line[1])
                
            if (instruction == "addx"):
                cycle += 1
                if (cycle in cycles):
                    sum_signal_strengths += (cycle * x)  

                x += value

    return sum_signal_strengths

def draw(screen, x, cycle):
    sprite_pos = [x-1,x,x+1]
    row = ceil(cycle/40) - 1
    column = (cycle - 1) % 40

    if column in sprite_pos:
        screen[row][column] = '#'

    return screen

def part_two(input_file):
    width = 40
    height = 6

    screen = [x[:] for x in [['.'] * width] * height]  

    with open(input_file) as f:
        instructions = []
        for line in f:
            line = line.strip().split(' ')
            instruction = line[0]
            if (len(line) > 1):
                value = line[1]

            instructions.append(line)

        x = 1
        cycle = 0

        while(len(instructions) > 0):
            cycle += 1
            screen = draw(screen, x, cycle)

            line = instructions.pop(0)
            instruction = line[0]

            if (len(line) > 1):
                value = int(line[1])

            if (instruction == "addx"):
                cycle += 1
                screen = draw(screen, x, cycle)
                x += value

    return screen


def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 13140
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    print("Test Part 2")
    for row in part_two(test):
        print (''.join(row))

    print("Input Part 2")
    for row in part_two(input):
        print (''.join(row))

if __name__ == '__main__':
    main()