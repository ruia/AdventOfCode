import queue

def part_one(input_file):
    row_of_crates = []
    procedures = []
    number_of_stacks = []
    stack_of_crates = []

    with open(input_file) as f:
        movements = False
        line_number = 0

        for line in f:
            line_number += 1
    
            if (line == '\n'):
                movements = True

            if not movements:
                line = list(line[i:i+3].strip().replace('[','').replace(']','') for i in range(0, len(line), 4))
                if not line[0].isnumeric():
                    row_of_crates.append(line)
                else:
                    number_of_stacks = line
            else:
                line = line.strip().split()

                if line:
                    # ['move', '1', 'from', '2', 'to', '1']
                    procedures.append([line[1], line[3], line[5]])

            line_number += 1
    
    row_of_crates.reverse()
    for i in number_of_stacks:
        stack_of_crates.append(queue.LifoQueue())

    for row in row_of_crates:
        for i, crate in enumerate(row):
            if crate:
                stack_of_crates[i].put(crate)

    for procedure in procedures:
        move_quantity = int(procedure[0])
        from_crate = int(procedure[1])-1
        to_crate = int(procedure[2])-1

        for i in range(move_quantity):
            stack_of_crates[to_crate].put(stack_of_crates[from_crate].get())
            
    top_crates = ''

    for i in range(len(stack_of_crates)):
        top_crates += stack_of_crates[i].get()

    return top_crates


def part_two(input_file):  
    row_of_crates = []
    procedures = []
    number_of_stacks = []
    stack_of_crates = []

    with open(input_file) as f:
        movements = False
        line_number = 0

        for line in f:
            line_number += 1
    
            if (line == '\n'):
                movements = True

            if not movements:
                line = list(line[i:i+3].strip().replace('[','').replace(']','') for i in range(0, len(line), 4))
                if not line[0].isnumeric():
                    row_of_crates.append(line)
                else:
                    number_of_stacks = line
            else:
                line = line.strip().split()

                if line:
                    # ['move', '1', 'from', '2', 'to', '1']
                    procedures.append([line[1], line[3], line[5]])

            line_number += 1
    
    row_of_crates.reverse()
    for i in number_of_stacks:
        stack_of_crates.append(queue.LifoQueue())

    for row in row_of_crates:
        for i, crate in enumerate(row):
            if crate:
                stack_of_crates[i].put(crate)

    for procedure in procedures:
        move_quantity = int(procedure[0])
        from_crate = int(procedure[1])-1
        to_crate = int(procedure[2])-1

        tmp = []

        for i in range(move_quantity):
            tmp.append(stack_of_crates[from_crate].get())

        for i in range(len(tmp)):
            stack_of_crates[to_crate].put(tmp.pop())


    top_crates = ''
    
    for i in range(len(stack_of_crates)):
        top_crates += stack_of_crates[i].get()

    return top_crates

test = "input_test.txt"
input = "input.txt"

print(f"Total part 1 test: {part_one(test)}")
print(f"Total part 1 input: {part_one(input)}")
print(f"Total part 2 test: {part_two(test)}")
print(f"Total part 2 input: {part_two(input)}")