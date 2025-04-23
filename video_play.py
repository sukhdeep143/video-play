import tkinter as tk



class VideoPlayer:
    def __init__(self, root):
        self.root = root
        
        # This is the title of the application
        self.root.title("Video Player")
        
        # This is for the size of the app
        self.root.geometry("2000x1500")


if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
