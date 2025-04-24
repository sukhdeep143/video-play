import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tkinter Widget Demo")
root.geometry("500x500")

# Create a frame
frame = tk.Frame(root, bg="lightblue", bd=5)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Label
label = tk.Label(frame, text="Welcome to Tkinter!", font=("Helvetica", 16))
label.pack(pady=10)

# Canvas
canvas = tk.Canvas(frame, width=200, height=100, bg="white")
canvas.create_oval(20, 20, 180, 80, fill="skyblue")
canvas.pack(pady=10)

# Button click event
def on_click():
    label.config(text="Button Clicked!")

# Button
button = tk.Button(frame, text="Click Me", command=on_click)
button.pack(pady=10)

# Canvas click event
def on_canvas_click(event):
    x, y = event.x, event.y
    canvas.create_text(x, y, text="🖱️", fill="red")

canvas.bind("<Button-1>", on_canvas_click)

# Grid layout example
grid_label = tk.Label(frame, text="Grid of Buttons:")
grid_label.pack(pady=5)

grid_frame = tk.Frame(frame)
grid_frame.pack()

for i in range(3):
    for j in range(3):
        tk.Button(grid_frame, text=f"({i},{j})").grid(row=i, column=j, padx=5, pady=5)

# Place layout example
placed_label = tk.Label(frame, text="Placed Label", bg="yellow")
placed_label.place(x=180, y=350)

# Run the GUI
root.mainloop()
