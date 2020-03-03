

def directions1_in_directions2(directions1, directions2):
    directions = []
    if (directions1 != None and len(directions1) > 0):
        #if direction of food not in viable direction, remove option
        for direction in directions1:
            if (direction in directions2):
                directions.append(direction)

        return directions

    return None

def get_direction(x,y,x2,y2):
 
    directions = []

    #to the left
    if (x - x2 > 0):
        directions.append('left')

    #to the right
    elif (x - x2 < 0):
        directions.append('right')

    #to the top
    if (y - y2 > 0):
        directions.append('up')

    #to the bottom
    elif (y - y2 < 0):
        directions.append('down')

    return directions

def get_location_from_direction(direction, x, y):
    if (direction == 'up'):
        return (x,y-1)
    if (direction == 'down'):
        return (x,y+1)
    if (direction == 'left'):
        return (x-1,y)
    if (direction == 'right'):
        return (x+1,y)

    return None

def add_to_dict(x, y, dict):
    if (not (x,y) in dict):
        dict[(x,y)] = 1
    else:
        dict[(x,y)] += 1

#return true if path stuck between 2 walls
def check_if_path_in_between_walls(data, path, walls):
    additional_walls = walls[:]

    for i in range(len(data['you']['body']) - 1):
        #remove own body from single lane wall check, besides tail since not part of walls already
        additional_walls.remove((data['you']['body'][i]['x'], data['you']['body'][i]['y']))

    #add border to walls
    for i in range(data['board']['width']):
        additional_walls.append((i, -1))
        additional_walls.append((i, data['board']['height']))
    
    for i in range(data['board']['height']):
        additional_walls.append((-1, i))
        additional_walls.append((data['board']['width'], i))

    for i in range(1, len(path)):
        adjacent_x_axis_walls = 0
        adjacent_y_axis_walls = 0
        if ((path[i][0] + 1, path[i][1]) in additional_walls):
            adjacent_x_axis_walls += 1
        if ((path[i][0] - 1, path[i][1]) in additional_walls):
            adjacent_x_axis_walls += 1
        if ((path[i][0], path[i][1] + 1) in additional_walls):
            adjacent_y_axis_walls += 1
        if ((path[i][0], path[i][1] - 1) in additional_walls):
            adjacent_y_axis_walls += 1

        if (adjacent_x_axis_walls >= 2 or adjacent_y_axis_walls >= 2):
            #path in between 2 opposing walls
            return True

    return False

def determine_if__snake_growing(data, snake_index):
    if (len(data['board']['snakes'][snake_index]) > 2):
        t1_x = data['board']['snakes'][snake_index]['body'][len(data['board']['snakes'][snake_index]) - 1]['x']
        t1_y = data['board']['snakes'][snake_index]['body'][len(data['board']['snakes'][snake_index]) - 1]['y']
        t2_x = data['board']['snakes'][snake_index]['body'][len(data['board']['snakes'][snake_index]) - 2]['x']
        t2_y = data['board']['snakes'][snake_index]['body'][len(data['board']['snakes'][snake_index]) - 2]['y']
        if (t1_x == t2_x and t1_y == t2_y):
            return True
    return False