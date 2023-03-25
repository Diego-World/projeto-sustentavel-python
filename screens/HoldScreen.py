from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage

from Constants import OUTPUT_PATH, ASSETS_PATH


class HoldScreen:
    def __init__(self, master=None):
        self.window = master if master else Tk()
        self.window.geometry("1366x768+100+15")
        self.window.title("Recicla Machine")
        self.window.configure(bg="#FFFFFF")
        img = PhotoImage(file='colorful/Icone.png')
        self.window.tk.call('wm', 'iconphoto', self.window._w, img)

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        background = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = canvas.create_image(
            683.0,
            384.0,
            image=background
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("logo_recicla_machine.png"))
        image_2 = canvas.create_image(
            506.0,
            384.0,
            image=image_image_2
        )

        canvas.create_text(
            683.0,
            288.0,
            anchor="nw",
            text="Aguarde",
            fill="#000000",
            font=("Aldrich Regular", 60 * -1)
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            223.0,
            84.0,
            image=image_image_3
        )

        canvas.create_text(
            683.0,
            404.0,
            anchor="nw",
            text="ESTAMOS CRIANDO A SUA\nNOVA CONTA",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        self.window.resizable(False, False)
        self.window.mainloop()
