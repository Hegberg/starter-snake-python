import random

from app.survive import survival_choices

def get_move(data):
    #directions = ["up", "down", "left", "right"]
    directions = survival_choices(data) #get bad options, remove them from contention
    
    if (len(directions) <= 0):
        directions = ["up", "down", "left", "right"]

    direction = random.choice(directions)
    return direction