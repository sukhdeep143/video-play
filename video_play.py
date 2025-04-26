import tkinter as tk
from tkinter import filedialog
import vlc  # VLC binding for Python

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        self.root.geometry("2000x1500")

        # VLC player instance
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Frame for video
        self.video_panel = tk.Frame(self.root)
        self.video_panel.pack(fill=tk.BOTH, expand=1)

        # 🎮 Frame for control buttons
        controls = tk.Frame(self.root)
        controls.pack()

        # Add buttons (Play, Pause, Stop, Open)
        self.play_button = tk.Button(controls, text="Play", command=self.play_video)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(controls, text="Pause", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(controls, text="Stop", command=self.stop_video)
        self.stop_button.pack(side=tk.LEFT)

        self.open_button = tk.Button(controls, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT)

    
    def open_file(self):
        self.video_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.mkv")]
        )
        if self.video_path:  # If user selected a file
            media = self.instance.media_new(self.video_path)
            self.player.set_media(media)


    def play_video(self):
        pass

    def pause_video(self):
        pass

    def stop_video(self):
        pass

    

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
