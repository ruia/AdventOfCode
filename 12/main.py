import collections

def parse_input(input_file):
    grid = []
    start_pos = []
    start_height = ord('a')
    dest_pos = []
    dest_height = ord('z')

    with open(input_file) as f:
        for row, line in enumerate(f):
            line = line.strip()
            grid.append([])
            for i in range(len(line)):
                if (line[i] == 'S'):
                    start_pos = [row, i]
                    grid[row].append('a')
                elif (line[i] == 'E'):
                    dest_pos = [row, i]
                    grid[row].append('z')
                else:
                    grid[row].append(line[i])
    
    return grid, start_pos, start_height, dest_pos, dest_height

dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

def isValid(grid, vis, row, col, x, y):
   
    # If cell lies out of bounds
    if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
        return False
 
    # If cell is already visited
    if ((row,col) in vis):
        return False

    cur_height = ord(grid[x][y])
    adj_height = ord(grid[row][col])

    if (cur_height >= adj_height) or (cur_height+1 == adj_height):
        return True
    else:
        False
            
    # Otherwise
    return True

def BFS(grid, start_pos, dest_pos):
   
    # Stores indices of the matrix cells
    q = []
 
    # Mark the starting cell as visited
    # and push it into the queue
    row = start_pos[0]
    col = start_pos[1]
    q.append(( row, col ))

    vis = [[ 0 for i in range(len(grid[0]))] for i in range(len(grid))]

    vis[row][col] = True

    while (len(q) > 0):
        cell = q.pop(0)
        x = cell[0]
        y = cell[1]

        if [x, y] == dest_pos:
            return vis[[dest_pos[0]][dest_pos[1]]]
        #q.pop()
 
        # Go to the adjacent cells
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(grid, vis, adjx, adjy, x, y)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = vis[x][y]+1

def part_one(input_file) -> int:
    grid, start_pos, start_height, dest_pos, dest_height = parse_input(input_file)

    

    path2 = BFS(grid, dest_pos, start_pos)
    print(path2)
    print(len(path2))
    # print(path2)
    # print(len(path2))
    # # return len(path)

def main():
    test = "input_test.txt"
    input = "input.txt"

    #assert part_one(test) == 31
    print(f"Total part 1 test: {part_one(test)}")
    #print(f"Total part 1 input: {part_one(input)}")

    # assert part_two(test) == 2713310158
    # print(f"Total part 2 test: {part_two(test)}")
    # print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()