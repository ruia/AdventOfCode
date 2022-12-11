import operator
import math

class Monkey():
    def __init__(self, items, operation, operation_value, test_value, test_result_actions, inspect_count) -> None:
        self.items = items
        self.operation = operation
        self.operation_value = operation_value
        self.test_value = test_value
        self.test_result_actions = test_result_actions
        self.inspect_count = inspect_count

def parse_input(input_file) -> tuple[list, int]:
    with open(input_file) as f:
        lines = f.readlines()
        monkeys = []
        i = 0
        while (len(lines) > 0):
            line = lines.pop(0).strip()
            if line:
                if (line.split(' ')[0] == 'Monkey'):
                    items = list(map(int, lines.pop(0).strip().split(': ')[1].split(',')))
                    operation, operation_value = lines.pop(0).strip().split(':')[1].split(' ')[-2:]
                    if (operation_value == 'old'):
                        operation_value = -1
                    else:
                        operation_value = int(operation_value)
                    test_value = int(lines.pop(0).strip().split(' ')[-1])
                    test_result_actions = []
                    test_result_actions.append(int(lines.pop(0).strip().split(' ')[-1]))
                    test_result_actions.append(int(lines.pop(0).strip().split(' ')[-1]))
                    monkeys.append(Monkey(items, operation, operation_value, test_value, test_result_actions, 0))
        
        lcm = math.lcm(*[monkey.test_value for monkey in monkeys])
        return monkeys, lcm

def perform_operation(item, operation, operation_value, lcm) -> int:
    ops = { '+': operator.add, '*': operator.mul }

    if(operation_value == -1):
        operation_value = item
      
    return (ops[operation](item, operation_value)) % lcm

def part_one(input_file) -> int:
    monkeys, lcm = parse_input(input_file)
    round_count = 0
    inspect_count = []

    while (round_count < 20):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                item = monkey.items.pop(0)
                item = perform_operation(item, monkey.operation, monkey.operation_value, lcm) // 3
                if ((item % monkey.test_value) == 0):
                    dest_monkey = monkey.test_result_actions[0]
                else:
                    dest_monkey = monkey.test_result_actions[1]
                monkey.inspect_count += 1
                monkeys[dest_monkey].items.append(item)    
        round_count += 1

    for  monkey in monkeys:
        inspect_count.append(monkey.inspect_count)

    inspect_count.sort(reverse = True)
    return inspect_count[0] * inspect_count[1]

def part_two(input_file) -> int:
    monkeys, lcm = parse_input(input_file)
    round_count = 0
    inspect_count = []

    while (round_count < 10000):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                item = monkey.items.pop(0)
                item = perform_operation(item, monkey.operation, monkey.operation_value, lcm)
                if ((item % monkey.test_value) == 0):
                    dest_monkey = monkey.test_result_actions[0]
                else:
                    dest_monkey = monkey.test_result_actions[1]
                monkey.inspect_count += 1
                monkeys[dest_monkey].items.append(item)    

        round_count += 1

    for  monkey in monkeys:
        inspect_count.append(monkey.inspect_count)

    inspect_count.sort(reverse = True)
    return inspect_count[0] * inspect_count[1]

def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 10605
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    assert part_two(test) == 2713310158
    print(f"Total part 2 test: {part_two(test)}")
    print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()