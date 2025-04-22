import tkinter as tk

root = tk.Tk()  # Main window
root.title("My First GUI")
root.geometry("300x200")  # Width x Height

frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(frame, text="Click Me", command=lambda: print("Button clicked!"))
button.pack(pady=5)

canvas = tk.Canvas(frame, width=100, height=100, bg="white")
canvas.create_oval(10, 10, 90, 90, fill="red")
canvas.pack(pady=5)


root.mainloop()
