def move_knot(leading_knot, following_knot):
    #its in the same x or y
    if ((leading_knot[0] == following_knot[0]) or (leading_knot[1] == following_knot[1])):
        if (leading_knot[1] > following_knot[1] + 1):
            following_knot[1] += 1
        elif (leading_knot[1] < following_knot[1] - 1):
            following_knot[1] -= 1
        elif (leading_knot[0] < following_knot[0] - 1):
            following_knot[0] -= 1
        elif (leading_knot[0] > following_knot[0] + 1):
            following_knot[0] += 1
    #diagonal
    else:
        #diag up right
        if (((leading_knot[0] > following_knot[0]) and (leading_knot[1] > following_knot[1] + 1)) or
            ((leading_knot[0] > following_knot[0] + 1) and (leading_knot[1] > following_knot[1]))):
            following_knot[0] += 1
            following_knot[1] += 1
        #diag up left 
        elif (((leading_knot[0] < following_knot[0] - 1) and (leading_knot[1] > following_knot[1])) or 
                ((leading_knot[0] < following_knot[0]) and (leading_knot[1] > following_knot[1] + 1))):
            following_knot[0] -= 1
            following_knot[1] += 1
        #diag down right
        elif (((leading_knot[0] > following_knot[0] + 1) and (leading_knot[1] < following_knot[1])) or
                (leading_knot[0] > following_knot[0]) and (leading_knot[1] < following_knot[1] - 1)):
            following_knot[0] += 1
            following_knot[1] -= 1
        #diag down left
        elif (((leading_knot[0] < following_knot[0] - 1) and (leading_knot[1] < following_knot[1])) or 
                ((leading_knot[0] < following_knot[0]) and (leading_knot[1] < following_knot[1] - 1))):
            following_knot[0] -= 1
            following_knot[1] -= 1

    return following_knot

def part_one(input_file):
    head_current_position = [0,0]
    tail_current_position = [0,0]

    visited_positions = []
    visited_positions.append([0,0])

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            direction, count = line.split(' ')
            for i in range(int(count)):
                if (direction == 'U'):
                    head_current_position[1] += 1
                elif (direction == 'D'):
                    head_current_position[1] -= 1
                elif (direction == 'L'):
                    head_current_position[0] -= 1
                elif (direction == 'R'):
                    head_current_position[0] += 1
                    
                tail_current_position = move_knot(head_current_position, tail_current_position)

                if (tail_current_position not in visited_positions):
                    visited_positions.append(tail_current_position[:])
  
    return len(visited_positions)

def part_two(input_file):
    knots = []
    for i in range(10):
        knots.append([0,0])

    visited_positions = []
    visited_positions.append([0,0])

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            direction, count = line.split(' ')
            for i in range(int(count)):            
                if (direction == 'U'):
                    knots[0][1] += 1
                elif (direction == 'D'):
                    knots[0][1] -= 1
                elif (direction == 'L'):
                    knots[0][0] -= 1
                elif (direction == 'R'):
                    knots[0][0] += 1

                j = 1
                while(j < 10):
                    knots[j] = move_knot(knots[j-1], knots[j])
                    j += 1

                if (knots[9] not in visited_positions):
                    visited_positions.append(knots[9][:])
  
    return len(visited_positions)

def main():

    test = "input_test.txt"
    test2 = "input_test2.txt"
    input = "input.txt"

    assert part_one(test) == 13
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    assert part_two(test2) == 36
    print(f"Total part 2 test: {part_two(test2)}")
    print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()