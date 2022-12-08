def part_one(input_file):
    grid = []
    visible_trees = 0

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            grid.append(list(map(int, line)))

        rows = len(grid)
        for row in range(rows):
            columns = len(grid[row])
            for column in range(columns):
                if ((row == 0) or (row == rows-1)):
                    visible_trees += 1 
                elif (((column == 0) or (column == columns-1)) and ((row > 0) or (row < rows-1))):
                    visible_trees += 1
                else:
                   #inner trees
                    visible_up, visible_down, visible_left, visible_right = True, True, True, True
                    # look up 
                    for i in range(row-1, -1, -1):
                        if (grid[row][column] <= grid[i][column]):
                            visible_up = False
                            break

                    # look down     
                    for i in range(row+1, rows):
                        if (grid[row][column] <= grid[i][column]):
                            visible_down = False
                            break

                    # look left
                    for i in range(column-1, -1, -1):
                        if (grid[row][column] <= grid[row][i]):
                            visible_left = False
                            break

                    # look right
                    for i in range(column+1, columns):
                        if (grid[row][column] <= grid[row][i]):
                            visible_right = False
                            break

                    if visible_up or visible_down or visible_left or visible_right:
                        visible_trees += 1

    return visible_trees

def part_two(input_file):  
    grid = []
    scenic_score = 0
    top_score = 0

    with open(input_file) as f:
        for line in f:
            line = line.strip()
            grid.append(list(map(int, line)))

        rows = len(grid)
        for row in range(rows):
            columns = len(grid[row])
            for column in range(columns):
                if ((row > 0) and (row < rows-1)) and ((column > 0) and (column < columns-1)):
                    #inner trees
                    score_up, score_down, score_left, score_right = 0, 0, 0, 0
                    # look up 
                    for i in range(row-1, -1, -1):
                        score_up += 1
                        if (grid[row][column] <= grid[i][column]):
                            break
                            
                    # look down     
                    for i in range(row+1, rows):
                        score_down += 1
                        if (grid[row][column] <= grid[i][column]):
                            break

                    # look left
                    for i in range(column-1, -1, -1):
                        score_left += 1
                        if (grid[row][column] <= grid[row][i]):
                            break

                    # look right
                    for i in range(column+1, columns):
                        score_right += 1
                        if (grid[row][column] <= grid[row][i]):
                            break

                    scenic_score = score_up * score_down * score_left * score_right
                    if (scenic_score > top_score):
                        top_score = scenic_score

    return top_score


def main():
    test = "input_test.txt"
    input = "input.txt"

    assert part_one(test) == 21
    print(f"Total part 1 test: {part_one(test)}")
    print(f"Total part 1 input: {part_one(input)}")

    assert part_two(test) == 8
    print(f"Total part 2 test: {part_two(test)}")
    print(f"Total part 2 input: {part_two(input)}")


if __name__ == '__main__':
    main()