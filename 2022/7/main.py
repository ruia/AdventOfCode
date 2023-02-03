from collections import defaultdict

def part_one(input_file):
    total_size = 0
    dir_sizes = defaultdict(int)

    with open(input_file) as f:
        pwd = []
        dir_sizes = defaultdict(int)

        is_ls = False

        for line in f:
            line = line.strip()
            # print(line)
            if (line[0:4] == '$ cd'):
                tmp = line.split(' ')
                cmd = tmp[1]
                arg = tmp[2]
                
                if (arg == '/'):
                    pwd.append(arg)
                elif (arg == '..'):
                    pwd.pop()
                else:
                    pwd.append('/'+arg)

                cur_pwd = ' '.join(pwd).replace(' ','').replace('//','/')
                dir_sizes[cur_pwd] += 0

            elif (line[0:4] == '$ ls'):
                is_ls = True  
            
            elif (is_ls):
                if (line[0].isnumeric()):
                    file = line.split(' ')
                    cur_pwd = ' '.join(pwd).replace(' ','').replace('//','/')
                    dir_sizes[cur_pwd] += int(file[0])

                    if cur_pwd != '/':
                        dir_sizes['/'] += int(file[0])

        for dir in dir_sizes:
            if (dir != '/'):
                for tmp in dir_sizes:
                    if ((tmp != '/') and (dir != tmp)):
                        if dir in tmp:
                            dir_sizes[dir] += dir_sizes[tmp]

        for dir in dir_sizes:
            if (dir_sizes[dir] <= 100000):
                total_size += dir_sizes[dir]

    return total_size


def part_two(input_file):  
    total_size = 0
    filesystem_size = 70000000
    update_size = 30000000

    dir_sizes = defaultdict(int)

    with open(input_file) as f:
        pwd = []
        dir_sizes = defaultdict(int)

        is_ls = False

        for line in f:
            line = line.strip()
            # print(line)
            if (line[0:4] == '$ cd'):
                tmp = line.split(' ')
                cmd = tmp[1]
                arg = tmp[2]
                
                if (arg == '/'):
                    pwd.append(arg)
                elif (arg == '..'):
                    pwd.pop()
                else:
                    pwd.append('/'+arg)

                cur_pwd = ' '.join(pwd).replace(' ','').replace('//','/')
                dir_sizes[cur_pwd] += 0

            elif (line[0:4] == '$ ls'):
                is_ls = True  
            
            elif (is_ls):
                if (line[0].isnumeric()):
                    file = line.split(' ')
                    cur_pwd = ' '.join(pwd).replace(' ','').replace('//','/')
                    dir_sizes[cur_pwd] += int(file[0])

                    if cur_pwd != '/':
                        dir_sizes['/'] += int(file[0])

        for dir in dir_sizes:
            if (dir != '/'):
                for tmp in dir_sizes:
                    if ((tmp != '/') and (dir != tmp)):
                        if dir in tmp:
                            dir_sizes[dir] += dir_sizes[tmp]
        
        unused_space = filesystem_size - dir_sizes['/']
        needed = update_size - unused_space
        
        available_for_deletion = []

        for dir in dir_sizes:
            if (dir_sizes[dir] > needed):
                available_for_deletion.append(dir_sizes[dir])

        available_for_deletion.sort()

        return available_for_deletion[0]
        


def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 95437
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    assert part_two(test) == 24933642
    print(f"Total part 2 test: {part_two(test)}")
    print(f"Total part 2 input: {part_two(input)}")


if __name__ == '__main__':
    main()