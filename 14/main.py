def part_one(input_file):
    units_of_sand = 0
    with open(input_file) as f:
        cave_system = []
        sand_entry_point = [6,0] # CHANGE LATER 500,0
        
        lines = f.readlines()

        max_rows = 0
        max_columns = 0

        resting_sand = 0

        for line in lines:
            line = line.strip().split(' -> ')
            for item in line:
                item = list(map(int,item.split(',')))
                if (int(item[1]) > max_rows):
                    max_rows = item[1]
                if (int(item[0]) > max_columns):
                    max_columns = item[0]
        
        for row in range(max_rows+1):
            cave_system.append([])
            for col in range(max_columns+1):
                cave_system[row].append([])
                cave_system[row][col] = '.'

        cave_system[sand_entry_point[1]][sand_entry_point[0]] = '+'

        for line in lines:
            line = line.strip().split(' -> ')
            path_coordinates = []
            for item in line:
                item = list(item.split(','))
                path_coordinates.append([int(item[0]), int(item[1])])
                
            for i, coord in enumerate(path_coordinates):
                cave_system[coord[1]][coord[0]] = '#'
                if (i > 0):
                    prev = path_coordinates[i-1]
                    cave_system = draw_path(cave_system, prev, coord)

        
        while(sand_fall(cave_system, sand_entry_point)):
                resting_sand += 1


    print_cave(cave_system)
    print(resting_sand)
    return units_of_sand  



def sand_fall(cave_system, sand_position):
    obstacles = ['#', 'o']
    sand_x, sand_y = sand_position
    result = False
    
    while(True):
        sand_y += 1
        if ((sand_x < 0) and (sand_x >= len(cave_system[0])) and (sand_y < 0) and (sand_y > len(cave_system))) or (sand_x-1 < 0 ) :
            return False
    
            
        if (cave_system[sand_y+1][sand_x] in obstacles):

            if (cave_system[sand_y+1][sand_x-1] not in obstacles):
                result = sand_fall(cave_system, [sand_x-1, sand_y])
            elif (cave_system[sand_y+1][sand_x+1] not in obstacles):
                result = sand_fall(cave_system, [sand_x+1, sand_y])
            else:
                cave_system[sand_y][sand_x] = 'o'
                return True
                
        if result:
            return True


def draw_path(cave_system, ori, dest):
    ori_x = ori[0]
    ori_y = ori[1]

    dest_x = dest[0]
    dest_y = dest[1]
    
    if (ori_x <= dest_x):
        stop_x = dest_x+1
        step_x = 1
    else:
        stop_x = dest_x-1
        step_x = -1

    if (ori_y <= dest_y):
        stop_y = dest_y+1
        step_y = 1
    else:
        stop_y = dest_y-1 
        step_y = -1
        
    for y in range(ori_y, stop_y, step_y):
        for x in range(ori_x, stop_x, step_x):
            cave_system[y][x] = '#'

    return cave_system

def print_cave(cave):
    for row in cave:
        print(row)

def main():
    test = "input_test.txt"
    test = "input_test_min.txt"
    input = "input.txt"


    # assert part_one(test) == 24
    print(f"Total part 1 test: {part_one(test)}")
    # print(f"Total part 1 input: {part_one(input)}")
    # assert part_two(test) == 140
    # print(f"Total part 2 test: {part_two(test)}")
    # print(f"Total part 2 input: {part_two(input)}")

if __name__ == '__main__':
    main()