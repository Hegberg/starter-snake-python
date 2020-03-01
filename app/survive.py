

def survival_choices(data):
    directions = check_bounds(data)

    directions = check_self_collisions(directions, data)
    directions = check_snake_collisions(directions, data)

    return directions

def check_bounds(data):
    directions = ["up", "down", "left", "right"]
    #check if space above us is on board
    if (data['board']['height'] - data['you']['body'][0]['y'] <= 1):
        directions.remove("up")

    #check if not on bottom row
    if (data['you']['body'][0]['y'] <= 0):
        directions.remove("down")

    #check if not on right wall
    if (data['board']['width'] - data['you']['body'][0]['x'] <= 1):
        directions.remove("right")
    
    #check if not on left wall
    if (data['you']['body'][0]['x'] <= 0):
        directions.remove("left")

    return directions

def check_self_collisions(directions, data):
    x = data['you']['body'][0]['x']
    y = data['you']['body'][0]['y']

    for i in range(1, len(data['you']['body'])):
        collision = check_beside_self(x,y,data['you']['body'][i]['x'],data['you']['body'][i]['y'])
        if (collision != 0 and collision in directions):
            directions.remove(collision)

    return directions

def check_snake_collisions(directions, data):
    x = data['you']['body'][0]['x']
    y = data['you']['body'][0]['y']

    for j in range(len(data['board']['snakes'])):
        #if snake is self, ignore
        if (data['board']['snakes'][j]['id'] == data['you']['id']):
            continue

        for i in range(0, len(data['board']['snakes'][j])):
            collision = check_beside_self(x,y,data['board']['snakes'][j]['body'][i]['x'],data['board']['snakes'][j]['body'][i]['y'])
            if (collision != 0 and collision in directions):
                directions.remove(collision)

    return directions

def check_beside_self(x,y,x2,x2):
    #to the direct left
    if (x - x2 == 1 and y - y2 == 0):
        return 'left'

    #to the direct right
    if (x - x2 == -1 and y - y2 == 0):
        return 'right'

    #to the direct bottom
    if (x - x2 == 0 and y - y2 == 1):
        return 'down'

    #to the direct top
    if (x - x2 == 0 and y - y2 == -1):
        return 'up'

    #nothing directly beside
    return 0