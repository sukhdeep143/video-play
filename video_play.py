import tkinter as tk
from tkinter import filedialog
import vlc
import os
import platform  # ✅ For OS detection

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        
        # This is the title of the application
        self.root.title("Video Player")
        
        # This is for the size of the app
        self.root.geometry("2000x1500")

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Video panel
        self.video_panel = tk.Frame(self.root)
        self.video_panel.pack(fill=tk.BOTH, expand=1)

        # Controls
        controls = tk.Frame(self.root)
        controls.pack()

        self.play_button = tk.Button(controls, text="Play", command=self.play_video)
        self.play_button.pack(side=tk.LEFT)

        self.pause_button = tk.Button(controls, text="Pause", command=self.pause_video)
        self.pause_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(controls, text="Stop", command=self.stop_video)
        self.stop_button.pack(side=tk.LEFT)

        self.open_button = tk.Button(controls, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT)

        self.video_path = None

        # Update UI to ensure the panel is rendered
        self.root.update()
        self.embed_video_panel()

    def embed_video_panel(self):
        system = platform.system()
        video_id = self.video_panel.winfo_id()

        if system == "Windows": # for Windows
            self.player.set_hwnd(video_id)
        elif system == "Linux": # For Linux
            self.player.set_xwindow(video_id)
        elif system == "Darwin":  # For macOS
            self.player.set_nsobject(video_id)
        else:
            print("Unsupported platform for video embedding.")

    def open_file(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if self.video_path:
            media = self.instance.media_new(self.video_path)
            self.player.set_media(media)
            self.play_video()

    def play_video(self):
        if self.video_path:
            self.player.play()

    def pause_video(self):
        self.player.pause()

    def stop_video(self):
        self.player.stop()

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
