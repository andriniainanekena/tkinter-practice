import tkinter as tk

from models import Connection, Hub


class GraphViewer:
    def __init__(
        self,
        hubs: list[Hub],
        connections: list[Connection],
    ) -> None:
        self.hubs = hubs
        self.connections = connections

        self.root = tk.Tk()
        self.root.title("Hello world")

        self.canvas = tk.Canvas(
            self.root,
            width=900,
            height=600,
            background="white",
        )
        self.canvas.pack(fill="both", expand=True)

        self.scale = 80
        self.offset_x = 100
        self.offset_y = 350

        self.draw()

    def to_canvas(self, x: float, y: float) -> tuple[float, float]:
        canvas_x = self.offset_x + x * self.scale
        canvas_y = self.offset_y - y * self.scale
        return canvas_x, canvas_y

    def draw(self) -> None:
        self.canvas.delete("all")

        hub_by_name = {
            hub.name: hub
            for hub in self.hubs
        }

        # Draw connections first so hubs appear above the lines.
        for connection in self.connections:
            source = hub_by_name[connection.source]
            destination = hub_by_name[connection.destination]

            x1, y1 = self.to_canvas(source.x, source.y)
            x2, y2 = self.to_canvas(destination.x, destination.y)

            self.canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                width=3,
                fill="gray",
            )

        # Draw hubs.
        radius = 22

        for hub in self.hubs:
            x, y = self.to_canvas(hub.x, hub.y)

            self.canvas.create_oval(
                x - radius,
                y - radius,
                x + radius,
                y + radius,
                fill=hub.color,
                outline="black",
                width=2,
            )

            self.canvas.create_text(
                x,
                y - radius - 15,
                text=hub.name,
                font=("Arial", 11, "bold"),
            )

    def run(self) -> None:
        self.root.mainloop()
