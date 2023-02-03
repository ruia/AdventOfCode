import re



def part_one(input_file):
    sensors = []
    beacons = []
    grid = []

    shift_col = 10
    shift_row = 10

    with open(input_file) as f:
        for line in f:
            re.split(': | , | =', line.strip())
            line = re.split(': |, |=', line.strip())
            sensors.append([int(line[1]), int(line[3])])
            beacons.append([int(line[-3]), int(line[-1])])

        min_col, max_col, min_row, max_row = 0, 0, 0, 0

        for element in sensors:
            column = element[0]
            row = element[1]
            if (column < min_col):
                min_col = column
            else:
                max_col = column
            
            if (row < min_row):
                min_row = column
            else:
                max_row = row

        for element in beacons:
            column = element[0]
            row = element[1]
            if (column < min_col):
                min_col = column
            elif (column > max_col):
                max_col = column
            
            if (row < min_row):
                min_row = column
            elif (row > max_row):
                max_row = row

        if (min_col < 0):
            shift_col += abs(min_col)
            max_col += shift_col
            min_col = 0
        
        if (min_row < 0):
            shift_row += abs(min_row)
            max_row += shift_row
            min_row = 0

        for row in range(min_row, max_row+21):
            grid.append([])
            for column in range(min_col, max_col+21):
                grid[row].append([])
                grid[row][column] = '.'
        
        for element in sensors:
            col_sensor = element[0]
            row_sensor = element[1]
            grid[row_sensor+shift_row][col_sensor+shift_col] = 'S'
            draw_diamond(grid, [col_sensor, row_sensor], shift_col, shift_row)

        for element in beacons:
            col_beacon = element[0]
            row_beacon = element[1]
            grid[row_beacon+shift_row][col_beacon+shift_col] = 'B'

        print_grid(grid)

        count = 0
        for col in grid[10+shift_row]:
            if col == '#':
                count += 1

        print(count)
        print(grid[10+shift_row])


def print_grid(grid):
    for row in grid:
        for column in row:
            print(column, end=' ')
        print()

def draw_diamond(grid, start, shift_col, shift_row):

    start = [start[0]+shift_col-9,start[1]+shift_row-9]

    for row in range(9+1):
        for column in range(8-row+1,9+row+1):
            if grid[start[1]+row][start[0]+column] == '.':
                grid[start[1]+row][start[0]+column] = '#'

    for row in range(9):
        for column in range(8-row+1,9+row+1):
            if grid[start[1]-row-shift_row-9-6][start[0]+column] == '.':
                grid[start[1]-row-shift_row-9-6][start[0]+column] = '#'

def main():
    test = "input_test.txt"
    input = "input.txt"

    #assert part_one(test) == 13
    print(f"Total part 1 test: {part_one(test)}")
    # print(f"Total part 1 input: {part_one(input)}")

    # assert part_two(test) == 140
    # print(f"Total part 2 test: {part_two(test)}")
    # print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()