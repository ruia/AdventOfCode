def part_one(input_file):
    jobs = {}
    with open(input_file) as f:
        for line in f:
            line = line.strip().split(': ')
            jobs[line[0]] = line[1]

        all_digit = False

        while (not all_digit):
            for monkey in reversed(jobs):
                if not str(jobs[monkey]).isdigit():
                    tmp = jobs[monkey].split(' ')
                    if str(jobs[tmp[0]]).isdigit() and str(jobs[tmp[2]]).isdigit():
                        jobs[monkey] = int(eval(str(jobs[tmp[0]]) + tmp[1] + str(jobs[tmp[2]])))
            tmp = []
            for monkey in jobs:
                if str(jobs[monkey]).isdigit():
                   tmp.append(True)
                else:
                    tmp.append(False)

            if not False in tmp:
                all_digit = True

        return jobs['root']

def part_two(input_file):
    jobs = {}
    with open(input_file) as f:
        for line in f:
            line = line.strip().split(': ')
            if (line[0] == 'root'):
                jobs[line[0]] = line[1].replace('+', '=')
            else:
                jobs[line[0]] = line[1]

        all_digit = False
        while (not all_digit):
            for monkey in reversed(jobs):
                if not str(jobs[monkey]).isdigit() and str(jobs[monkey] != 'humn'):
                    tmp = jobs[monkey].split(' ')
                    if str(jobs[tmp[0]]).isdigit() and str(jobs[tmp[2]]).isdigit():
                        jobs[monkey] = int(eval(str(jobs[tmp[0]]) + tmp[1] + str(jobs[tmp[2]])))
            tmp = []
            for monkey in jobs:
                if str(jobs[monkey]).isdigit():
                   tmp.append(True)
                else:
                    tmp.append(False)

            if not False in tmp:
                all_digit = True

        return jobs['root']

def main():
    test = "input_test.txt"
    input = "input.txt"
    # test = "input_test_min.txt"

    assert part_one(test) == 152
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    #assert part_two(test) == 301
    print(f"Total part 2 test: {part_two(test)}")
    # print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()