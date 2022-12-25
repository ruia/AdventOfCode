def part_one(input_file):
    sum_decimal = 0

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            for i, char in enumerate(line):
                if char == '=':
                    val = -2
                elif char == '-':
                    val = -1
                else:
                    val = int(char)
                
                sum_decimal += val * pow(5, len(line)-i-1)
            
        return sum_decimal
        

def main():
    test = "input_test.txt"
    input = "input.txt"
    # test = "input_test_min.txt"

    # assert part_one(test) == '2=-1=0'
    print(f"Total part 1 test: {part_one(test)}")
    # print(f"Total part 1 input: {part_one(input)}")

    # assert part_two(test) == 93
    # print(f"Total part 2 test: {part_two(test)}")
    # print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()