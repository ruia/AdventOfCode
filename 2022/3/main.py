def part_one(input_file):
    with open(input_file) as f:
        total = 0
        for line in f:
            line = line.strip()
            first_half, second_half = line[:len(line)//2], line[len(line)//2:]
            common_type = list(set(first_half).intersection(second_half))
            total_common = 0
            for x in common_type:
                if (x.isupper()):
                    total_common += ord(x)-38
                else:
                    total_common += ord(x)-96

            total += total_common

        print(f"Total Part One: {total}")

def part_two(input_file):  
    with open(input_file) as f:
        lines = f.readlines()
        group = []
        count = 0 
        total = 0
        for line in lines:
            count += 1
            line = line.strip()
            group.append(line)
            if (count == 3):
                common_type = list(set(group[0]).intersection(group[1], group[2]))
                total_common = 0
                for x in common_type:
                    if (x.isupper()):
                        total_common += ord(x)-38
                    else:
                        total_common += ord(x)-96
                total += total_common
                count = 0
                group = []
                
        print(f"Total Part Two: {total}")

file_in = "input.txt"
part_one(file_in)
part_two(file_in)