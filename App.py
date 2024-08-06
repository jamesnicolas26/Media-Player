import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class MediaPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Player")

        mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.play_button = tk.Button(self.root, text="Play", command=self.play_media)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_media)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_media)
        self.stop_button.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load Media", command=self.load_media)
        self.load_button.pack(pady=10)

    def play_media(self):
        if hasattr(self, 'media_file'):
            mixer.music.load(self.media_file)
            mixer.music.play()

    def pause_media(self):
        mixer.music.pause()

    def stop_media(self):
        mixer.music.stop()

    def load_media(self):
        self.media_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])

# Create the main window
root = tk.Tk()
app = MediaPlayer(root)
root.mainloop()
