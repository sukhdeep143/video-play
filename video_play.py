import tkinter as tk
from tkinter import filedialog
import vlc
import os
import platform
import threading
import time

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        self.root.geometry("1000x600")

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.video_panel = tk.Frame(self.root)
        self.video_panel.pack(fill=tk.BOTH, expand=1)

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

        # Progress bar (Scale)
        self.progress = tk.Scale(self.root, from_=0, to=1000, orient="horizontal", length=800, showvalue=0, command=self.seek)
        self.progress.pack()

        self.video_path = None
        self.updating_slider = False  # flag to prevent circular updates

        self.root.update()
        self.embed_video_panel()

        # Start thread to update progress bar
        self.update_thread = threading.Thread(target=self.update_progress, daemon=True)
        self.update_thread.start()

    def embed_video_panel(self):
        system = platform.system()
        video_id = self.video_panel.winfo_id()

        if system == "Windows":
            self.player.set_hwnd(video_id)
        elif system == "Linux":
            self.player.set_xwindow(video_id)
        elif system == "Darwin":
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

    def update_progress(self):
        while True:
            if self.player.is_playing():
                length = self.player.get_length()  # total length in ms
                if length > 0:
                    time_ms = self.player.get_time()
                    progress_value = int((time_ms / length) * 1000)
                    self.updating_slider = True
                    self.progress.set(progress_value)
                    self.updating_slider = False
            time.sleep(1)

    def seek(self, val):
        if not self.updating_slider:  # Avoid feedback loop
            length = self.player.get_length()
            if length > 0:
                new_time = int((int(val) / 1000) * length)
                self.player.set_time(new_time)

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
