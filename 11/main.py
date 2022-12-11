class Monkey():
    def __init__(self, items, operation, operation_value, test_value, test_result_actions) -> None:
        self.items = items
        self.operation = operation
        self.operation_value = operation_value
        self.test_value = test_value
        self.test_result_actions = test_result_actions

    def __str__(self) -> str:
        print(f"{self.items} - {self.operation}")

def parse_input(input_file) -> list:
    with open(input_file) as f:
        lines = f.readlines()
        monkeys = []
        i = 0
        while (len(lines) > 0):
            line = lines.pop(0).strip()
            if line:
                # print(line)
                if (line.split(' ')[0] == 'Monkey'):
                    items = list(map(int, lines.pop(0).strip().split(': ')[1].split(',')))
                    operation, operation_value = lines.pop(0).strip().split(':')[1].split(' ')[-2:]
                    test_value = int(lines.pop(0).strip().split(' ')[-1])
                    test_result_actions = []
                    test_result_actions.append(int(lines.pop(0).strip().split(' ')[-1]))
                    test_result_actions.append(int(lines.pop(0).strip().split(' ')[-1]))
                    monkeys.append(Monkey(items, operation, operation_value, test_value, test_result_actions))
        return monkeys

def part_one(input_file) -> int:
    monkeys = parse_input(input_file)
    print(monkeys[0])
    round_count = 0
    #while
    #for loop monkeys
    #if monkey.items > 0
        


def part_two(input_file):
    pass

def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 10605
    print(f"Total part 1 test: {part_one(test)}")
    # print(f"Total part 1 input: {part_one(input)}")

if __name__ == '__main__':
    main()