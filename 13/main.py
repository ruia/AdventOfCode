import itertools

def compare_packets(left, right):
    for combination in itertools.zip_longest(left, right, fillvalue=None):
        left_ele = combination[0]
        right_ele = combination[1]
        if (left_ele == None):
            return True
        elif (right_ele == None):
            return False
        elif (type(left_ele) == int) and (type(right_ele) == int):
            if (left_ele > right_ele):
                return False
            elif(left_ele < right_ele):
                return True
            else:
                continue
        elif (type(left_ele) == list) or (type(right_ele) == list):
            left_ele = as_list(left_ele)
            right_ele = as_list(right_ele)
            result = compare_packets(left_ele, right_ele)
            if (result == None):
                continue
            else:
                return result
        else:
            break

def as_list(x):
    if type(x) is list:
        return x
    else:
        return [x]

def part_one(input_file):
    sum_of_indices = 0
    data = []
    index = 0

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if (line):
                data.append(line)

    while (len(data) > 0):
        index += 1
        packet = []
        left = eval(data.pop(0))
        right = eval(data.pop(0))

        if compare_packets(left, right):
            sum_of_indices += index
    
    return sum_of_indices

def part_two(input_file):
    data = []

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if (line):
                data.append(line)
                
    data.append('[2]')
    data.append('[6]')
    
    packets = [eval(line) for line in data]

    divider = [[2], [6]]
    divider_indexes = []

    n = len(packets)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_packets(packets[j+1], packets[j]):
                packets[j], packets[j+1] = packets[j+1], packets[j]

    for i, packet in enumerate(packets):
        if (packet in divider):
            divider_indexes.append(i+1)

    return (divider_indexes[0]*divider_indexes[1])

def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 13
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}") # 4051 low # 4867 low 6543 low 6772

    assert part_two(test) == 140
    print(f"Total part 2 test: {part_two(test)}")
    print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()