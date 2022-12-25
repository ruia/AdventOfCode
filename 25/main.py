def part_one(input_file):
    sum_decimal = 0

    fuels = { '=': -2, '-': -1, '0': 0, '1': 1, '2': 2 }
    decimals = dict(map(reversed, fuels.items()))

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            for i, char in enumerate(line):
                sum_decimal += fuels[char] * pow(5, len(line)-i-1)
            
        ret = []

        while sum_decimal > 0:
            remain = sum_decimal % 5
            if remain > 2:
                sum_decimal += remain
                ret.append(decimals[remain - 5])
            else:
                ret.append(str(remain))

            sum_decimal //= 5    

    return ''.join(reversed(ret))
    

def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == '2=-1=0'
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    # assert part_two(test) == 93
    # print(f"Total part 2 test: {part_two(test)}")
    # print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()