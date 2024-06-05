import random

class GameLocations:
    """An instance of this class contains all the game locations."""
    def __init__(self):
        locations = random.sample(range(1, 31), 6) # Returns a list of random rooms
        self.userRoom = locations[0]
        self.wumpusRoom = locations[1]
        self.batRoom1 = locations[2]
        self.batRoom2 = locations[3]
        self.pitRoom1 = locations[4]
        self.pitRoom2 = locations[5]