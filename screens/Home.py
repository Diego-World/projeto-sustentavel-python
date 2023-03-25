import tkinter as tk
from logging import root
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
from tkVideoPlayer import TkinterVideo
from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import Access

def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

class Home(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Recicla Machine")
        img = PhotoImage(file='colorful/Icone.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, img)
        self.master.resizable(False, False)
        center_window(1366, 768)

        OUTPUT_PATH
        ASSETS_PATH

        def open_new_window():
            for widget in root.winfo_children():
                widget.destroy()
            self.destroy()
            Access.Acess(master)

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def loopVideo(event):
            videoplayer.play()

        canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = canvas.create_image(
            683.0,
            684.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            0.0,
            0.0,
            1366.0,
            601.0,
            fill="#64C562",
            outline="")

        videoplayer = TkinterVideo(master=self.master,scaled=True,anchor="nw",
                         padx=0, pady=0)
        videoplayer.load(r"home_page_videos/video.mp4")
        videoplayer.place(x=0, y=0, width=1366, height=601)
        videoplayer.play()


        start_usage_button = PhotoImage(
            file=relative_to_assets("start_usage_button.png"))
        button_1 = Button(
            self.master,
            image=start_usage_button,
            borderwidth=0,
            highlightthickness=0,
            command=open_new_window,
            relief="flat"
        )
        button_1.place(
            x=383.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        videoplayer.bind('<<Ended>>', loopVideo)
        self.master.mainloop()

root = tk.Tk()
Home(root)
root.mainloop()