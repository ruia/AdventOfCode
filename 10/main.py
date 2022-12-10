def part_one(input_file):
    with open(input_file) as f:
        lines = []
        for line in f:
            line = line.strip().split(' ')
            print(line)
            instruction = line[0]
            if (len(line) > 1):
                value = line[1]
            line.append[line]
        x = 1
        cycle = 1
        while(True):
            line = lines.pop(0)
            instruction = line[0]
            if (len(line) > 1):
                value = line[1]
            
            if (instruction == "noop"):
                continue
            elif (instruction == "addx"):





            # print(f"{instruction} - {value}")

    return x

def part_two(input_file):
    pass

def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 13140
    print(f"Total part 1 test: {part_one(test)}")
    # print(f"Total part 1 input: {part_one(input)}")

    # assert part_two(test2) == 36
    # print(f"Total part 2 test: {part_two(test2)}")
    # print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()