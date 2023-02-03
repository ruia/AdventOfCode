def part_one(input_file):
    with open(input_file) as f:
        for line in f:
            start_of_packet_marker = 4
            for i,_ in enumerate(line):
                marker = line[i:start_of_packet_marker]
                if (len(set(marker)) == len(marker)):
                    break
                else:
                    start_of_packet_marker += 1
        return start_of_packet_marker

def part_two(input_file):  
    with open(input_file) as f:
        for line in f:
            start_of_message_marker = 14
            for i,_ in enumerate(line):
                marker = line[i:start_of_message_marker]
                if (len(set(marker)) == len(marker)):
                    break
                else:
                    start_of_message_marker += 1
        return start_of_message_marker


def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 7
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    assert part_two(test) == 19
    print(f"Total part 2 test: {part_two(test)}")
    print(f"Total part 2 input: {part_two(input)}")


if __name__ == '__main__':
    main()