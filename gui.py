import tkinter as tk
from tkinter import Canvas
from map import Map

class MapGUI:
    def __init__(self, game_map: Map, master: tk.Tk):
        self.game_map = game_map
        self.master = master
        master.title("Story Mapper")

        self.canvas_width = 600
        self.canvas_height = 600
        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        master.update()  # Ensure window is fully rendered
        self.canvas_width = master.winfo_width()
        self.canvas_height = master.winfo_height()

        self.room_width = self.canvas_width / game_map.width
        self.room_height = self.canvas_height / game_map.height

        master.bind("<Configure>", self.on_resize)  # Bind the resize event

        self.draw_map()

    def draw_map(self):
        self.canvas.delete("all")  # Clear the canvas before redrawing
        for x in range(self.game_map.width):
            for y in range(self.game_map.height):
                room = self.game_map.get_room(x, y)
                if room:
                    x1 = x * self.room_width
                    y1 = y * self.room_height
                    x2 = (x + 1) * self.room_width
                    y2 = (y + 1) * self.room_height
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="black")

                    description = room.description
                    if len(description) > 25:
                        description = description[:23] + "..."

                    text = f"{room.name}\n{description}"

                    self.canvas.create_text(
                        (x1 + x2) / 2,
                        (y1 + y2) / 2,
                        text=text,
                        fill="black",
                        font=("Arial", 8),
                        justify=tk.CENTER  # Center align the text
                    )

    def on_resize(self, event):
        self.canvas_width = event.width
        self.canvas_height = event.height
        self.room_width = self.canvas_width / self.game_map.width
        self.room_height = self.canvas_height / self.game_map.height
        self.draw_map()

def run_gui(game_map: Map):
    root = tk.Tk()
    root.geometry("800x600")  # Set initial window size
    gui = MapGUI(game_map, root)
    root.mainloop()
