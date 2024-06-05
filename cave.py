import json
import random

class Cave:
    # Load room dictionaries
    @staticmethod
    def load_room_dicts():
        """Loads and returns all three possible room dictionary files."""
        with open("room_dic1.json", "r") as file:
            room_dic1 = json.load(file) # Loads first map
        with open("room_dic2.json", "r") as file:
            room_dic2 = json.load(file)  # Loads second map
        with open("room_dic3.json", "r") as file:
            room_dic3 = json.load(file)  # Loads third map
        return [room_dic1, room_dic2, room_dic3] # Returns a list of the three maps
    
    @staticmethod
    def random_dict():
        """Returns a random dictionary."""
        return random.choice(Cave.load_room_dicts())
    
    @staticmethod
    def open_one():
        """Returns the first (default) dictionary."""
        with open("room_dic1.json", "r") as file:
            room_dic1 = json.load(file) # Loads first map
        return room_dic1