from map import Map
from gui import run_gui
from typing import Tuple

def main() -> None:
    """Main entry point for the story mapper application."""
    try:
        # Create game map
        width = 5
        height = 5
        print(f"Creating map of size {width}x{height}...")
        game_map = Map(width, height)

        # Run the GUI
        run_gui(game_map)

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
