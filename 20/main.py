from math import floor

def part_one(input_file):

    with open(input_file) as f:
        original_encrypted_file = [int(line) for line in f]

        decrypted_file = [(index, item) for index, item in enumerate(original_encrypted_file)]

        for index, item in enumerate(original_encrypted_file):
            old_index =  decrypted_file.index((index,item))
            decrypted_file.remove((index, item))
            new_index = (old_index + item + len(original_encrypted_file) - 1) % (len(original_encrypted_file) - 1)
            decrypted_file.insert(new_index, (-1, item))

        count = 0 - decrypted_file.index((-1,0))
        sum_coords = 0
        while (count < 10000):
            for _, item in decrypted_file:
                if (count == 1000) or (count == 2000) or (count == 3000):
                    sum_coords += item              

                count += 1

        return sum_coords

def part_two(input_file):
    dec_key  = 811589153

    with open(input_file) as f:
        original_encrypted_file = [int(line) * dec_key for line in f]

        decrypted_file = [(index, item) for index, item in enumerate(original_encrypted_file)]

        for _ in range(10):
            for index, item in enumerate(original_encrypted_file):
                old_index =  decrypted_file.index((index,item))
                decrypted_file.remove((index, item))
                new_index = (old_index + item + len(original_encrypted_file) - 1) % (len(original_encrypted_file) - 1)
                decrypted_file.insert(new_index, (index, item))

        count = 0 - decrypted_file.index((original_encrypted_file.index(0),0))
        sum_coords = 0
        while (count < 10000):
            for _, item in decrypted_file:
                if (count == 1000) or (count == 2000) or (count == 3000):
                    sum_coords += item              

                count += 1

        return sum_coords


def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 3
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    assert part_two(test) == 1623178306
    print(f"Total part 2 test: {part_two(test)}")
    print(f"Total part 2 input: {part_two(input)}")

if __name__ == "__main__":
    main()