import tkinter as tk

root = tk.Tk()  # Main window
root.title("My First GUI")
root.geometry("300x200")  # Width x Height

frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame.pack(fill="both", expand=True)
