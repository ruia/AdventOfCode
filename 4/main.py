def part_one(input_file):
    with open(input_file) as f:
        overlap_count = 0
        for line in f:
            line = line.strip()
            section_one, section_two = line.split(",")[0].split("-"), line.split(",")[1].split("-")
            section_one, section_two = set(range(int(section_one[0]), int(section_one[1])+1)), set(range(int(section_two[0]), int(section_two[1])+1))
            overlap = set(section_one).intersection(section_two)
            if ((len(section_one) == len(overlap)) or (len(section_two) == len(overlap))):
                overlap_count += 1

        return overlap_count

def part_two(input_file):  
    with open(input_file) as f:
        overlap_count = 0
        for line in f:
            line = line.strip()
            section_one, section_two = line.split(",")[0].split("-"), line.split(",")[1].split("-")
            section_one, section_two = set(range(int(section_one[0]), int(section_one[1])+1)), set(range(int(section_two[0]), int(section_two[1])+1))
            overlap = set(section_one).intersection(section_two)
            if (len(overlap) > 0):
                overlap_count += 1

        return overlap_count

test = "input_test.txt"
input = "input.txt"
print(f"Total part 1 test: {part_one(test)}")
print(f"Total part 1 input: {part_one(input)}")
print(f"Total part 2 test: {part_two(test)}")
print(f"Total part 2 input: {part_two(input)}")