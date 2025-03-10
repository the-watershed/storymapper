from typing import List, Optional, Tuple
from room import Room

class Map:
    """Represents a 2D grid of rooms that form the game world."""
    
    def __init__(self, width: int, height: int):
        """Initialize a new map of the given dimensions.
        
        Args:
            width: The width of the map in rooms
            height: The height of the map in rooms
        """
        self.width = width
        self.height = height
        self.grid = self.generate_grid()
        self.connect_rooms()
    
    def generate_grid(self) -> List[List[Room]]:
        """Generate a grid of rooms.
        
        Returns:
            A 2D list of Room objects
        """
        return [[Room(x, y) for y in range(self.height)] for x in range(self.width)]
    
    def display_map(self) -> None:
        """Print a simple text representation of the map."""
        for row in self.grid:
            for room in row:
                inventory_count = len(room.inventory)
                mob_count = len(room.mobs)
                print(f"Room({room.x}, {room.y}) - Light: {room.light_value}, "
                      f"Weather: {room.weather_affected}, Items: {inventory_count}, Mobs: {mob_count}")
            print()
            
    def get_room(self, x: int, y: int) -> Optional[Room]:
        """Retrieve the room at the specified coordinates.
        
        Args:
            x: X-coordinate
            y: Y-coordinate
            
        Returns:
            Room object if coordinates are valid, None otherwise
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[x][y]
        return None
    
    def connect_rooms(self) -> None:
        """Connect all rooms to their adjacent neighbors."""
        for x in range(self.width):
            for y in range(self.height):
                current = self.grid[x][y]
                
                # Connect to east room
                if x < self.width - 1:
                    current.connect_room(self.grid[x+1][y], "east")
                
                # Connect to south room
                if y < self.height - 1:
                    current.connect_room(self.grid[x][y+1], "south")
    
    def find_path(self, start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Find a path between two points on the map.
        
        Args:
            start: The starting (x, y) coordinates
            end: The ending (x, y) coordinates
            
        Returns:
            List of (x, y) coordinates forming a path, or empty list if no path
        """
        # Simple breadth-first search implementation
        from collections import deque
        
        if not (0 <= start[0] < self.width and 0 <= start[1] < self.height and
                0 <= end[0] < self.width and 0 <= end[1] < self.height):
            return []
            
        visited = set()
        queue = deque([(start, [])])
        
        while queue:
            (x, y), path = queue.popleft()
            
            if (x, y) == end:
                return path + [(x, y)]
                
            if (x, y) in visited:
                continue
                
            visited.add((x, y))
            current = self.grid[x][y]
            
            for direction, next_room in current.exits.items():
                if next_room is not None and (next_room.x, next_room.y) not in visited:
                    queue.append(((next_room.x, next_room.y), path + [(x, y)]))
                    
        return []

    def resize(self, new_width: int, new_height: int) -> None:
        """Resize the map to the new dimensions.

        Args:
            new_width: The new width of the map in rooms
            new_height: The new height of the map in rooms
        """
        self.width = new_width
        self.height = new_height
        self.grid = self.generate_grid()  # Regenerate the grid with new dimensions
        self.connect_rooms()  # Reconnect the rooms
