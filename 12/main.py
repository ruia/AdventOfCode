def parse_input(input_file):
    grid = []
    start_pos = []
    start_height = 'a'
    dest_pos = []
    dest_height = 'z'

    with open(input_file) as f:
        for row, line in enumerate(f):
            line = line.strip()
            grid.append([])
            for i in range(len(line)):
                if (line[i] == 'S'):
                    start_pos = [row, i]
                    grid[row].append(start_height)
                elif (line[i] == 'E'):
                    dest_pos = [row, i]
                    grid[row].append(dest_height)
                else:
                    grid[row].append(line[i])
    
    return grid, start_pos, start_height, dest_pos, dest_height

def can_move(grid, cur_pos, dest_pos):
    cur_height = ord(grid[cur_pos[0]][cur_pos[1]])
    dest_height = ord(grid[dest_pos[0][dest_pos[1]]])

    if ((dest_height == cur_height + 1) or (dest_height < cur_height)):
        return True
    
    return False
    
def possible_moves(grid, cur_pos):
    moves = []
    
    x = cur_pos[0]
    y = cur_pos[1]

    max_x = len(grid[0])
    max_y = len(grid[0][0])

    if (x == 0):
        moves.append('D')
    elif (x == max_x):
        moves.append('U')
    elif (x > 0) and (x < len(grid[0])):
        moves.append('U')
        moves.append('D')
    
    if (y == 0):
        moves.append('R')
    elif (y == max_y):
        moves.append('L')
    else:
        moves.append('R')
        moves.append('L')

    return moves


def part_one(input_file) -> int:
    grid, start_pos, start_height, dest_pos, dest_height = parse_input(input_file)
    cur_pos = [0,0]
    all_moves = []

    while (True):
        # if (cur_pos == dest_pos):
        #     break
        moves_made = []
        # check possible moves
        # check if height allows move.
        #  add mvoes made to list
        #  uppon reaching dest add list of moves to all moves to determine the minimum dist




        moves = possible_moves(grid, cur_pos)
        
        # up
        if ():
            pass

    print(grid)
    print(grid[0][1])

def main():
    test = "input_test.txt"
    input = "input.txt"
    test = "C:\\Users\\ruial\\workspace\\adventofcode\\12\\input_test.txt"

    #assert part_one(test) == 31
    print(f"Total part 1 test: {part_one(test)}")
    # print(f"Total part 1 input: {part_one(input)}")

    # assert part_two(test) == 2713310158
    # print(f"Total part 2 test: {part_two(test)}")
    # print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()