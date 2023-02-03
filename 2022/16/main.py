import re

from dataclasses import dataclass

@dataclass
class Valve:
    name: str
    flow_rate: int
    tunnels: list
    is_open: bool = False

def part_one(input_file):
    with open('input_test.txt') as f:
        valves = {}
        for line in f:
            line = re.split(' |=', line.strip().replace(',', ''))
            valves[line[1]] = Valve(name=line[1], flow_rate=line[5], tunnels=line[10:])

    
    print(valves)


if __name__ == '__main__':
    test = "input_test.txt"
    input = "input.txt"

    #assert part_one(test) == 1651
    print(f"Total part 1 test: {part_one(test)}")
    # print(f"Total part 1 input: {part_one(input)}")

    # assert part_two(test) == 
    # print(f"Total part 2 test: {part_two(test)}")
    # print(f"Total part 2 input: {part_two(input)}")
