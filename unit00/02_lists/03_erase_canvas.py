import tkinter as tk

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(event):
    """Erase cells when dragging the eraser."""
    x, y = event.x, event.y
    item = canvas.find_closest(x, y)
    canvas.itemconfig(item, fill="red")  # Change the cell color to white

def main():
    global canvas
    root = tk.Tk()
    root.title("Eraser Canvas")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    # Draw the grid
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="yellow", outline="black")

    # Create an eraser
    canvas.bind("<B1-Motion>", erase)  # B1-Motion: Dragging with left mouse button

    root.mainloop()

if __name__ == '__main__':
    main()
