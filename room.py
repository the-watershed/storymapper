import random
from typing import List, Dict, Optional, Any
import json

with open("d:\\drevo\\OneDrive\\Documents\\.Documents\\repos\\storymapper\\map1.json", "r") as f:
    map_data = json.load(f)
    ROOM_DATA = map_data["rooms"]

class Room:
    """Represents a room in the game world with position and contents."""
    
    def __init__(self, x: int, y: int):
        """Initialize a new room at the given coordinates.
        
        Args:
            x: X-coordinate of the room
            y: Y-coordinate of the room
        """
        self.x = x
        self.y = y
        self.room_data = self.get_room_data()
        self.name = self.room_data["name"]
        self.description = self.room_data["description"]
        self.inventory = self.room_data["inventory"]
        self.npcs = self.room_data["npcs"]
        self.exits = self.room_data["exits"]
        self.light_value = self.generate_light_value()
        self.weather_affected = self.generate_weather_affected()
        self.conditions = self.generate_conditions()

    def get_room_data(self) -> Dict[str, Any]:
        """Get room data from the JSON file.
        
        Returns:
            A dictionary containing room data
        """
        return random.choice(ROOM_DATA)

    def generate_light_value(self) -> int:
        """Generate a random light value for the room.
        
        Returns:
            An integer from 0 (darkest) to 10 (brightest)
        """
        return random.randint(0, 10)

    def generate_weather_affected(self) -> bool:
        """Determine if the room is affected by weather.
        
        Returns:
            Boolean indicating if room is affected by weather
        """
        return random.choice([True, False])

    def generate_conditions(self) -> List[str]:
        """Generate random environmental conditions for the room.
        
        Returns:
            A list of conditions affecting the room
        """
        condition_options = ["wet", "foggy", "hot", "cold", "windy", "quiet", "noisy", "smoky"]
        num_conditions = random.randint(0, 2)
        return random.sample(condition_options, num_conditions) if num_conditions > 0 else []
    
    def connect_room(self, other: 'Room', direction: str) -> bool:
        """Connect this room to another in the specified direction.
        
        Args:
            other: The room to connect to
            direction: Direction of connection (north, east, south, west)
            
        Returns:
            True if connection was successful, False otherwise
        """
        if direction not in self.exits:
            return False
            
        opposite = {"north": "south", "south": "north", "east": "west", "west": "east"}
        self.exits[direction] = other
        other.exits[opposite[direction]] = self
        return True
