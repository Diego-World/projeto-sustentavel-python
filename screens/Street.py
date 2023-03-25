from Constants import ASSETS_PATH,OUTPUT_PATH
import json
import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage, messagebox

from Constants import ASSETS_PATH, OUTPUT_PATH
from Constants import DATA_STAGE_FILE
from keyboard import KeyboardOneEntry
from screens import HouseNumber


class Street(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        bg_image = PhotoImage(file=relative_to_assets('background.png'))
        pixel_color = "#" + "".join(map(lambda x: hex(x)[2:].zfill(2), bg_image.get(50, 100)))

        def on_button_click():
            street = entry_1.get()

            if street == "":
                messagebox.showerror("Erro", "Por favor, preencha o campo.")
            else:
                try:
                    with open(DATA_STAGE_FILE, "r") as f:
                        data = json.load(f)
                except:
                    data = []

                data["street"] = street

                with open(DATA_STAGE_FILE, "w") as f:
                    f.write(json.dumps(data))

                for widget in master.winfo_children():
                    widget.destroy()
                self.destroy()
                HouseNumber.HouseNumber(master)

        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )


        self.canvas.place(x = 0, y = 0)
        background = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = self.canvas.create_image(
            683.0,
            384.0,
            image=background
        )

        self.canvas.create_text(
            32.0,
            160.0,
            anchor="nw",
            text="Vamos criar o \nseu cadastro",
            fill="#000000",
            font=("Aldrich Regular", 60 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("logo_recicla_machine.png"))
        image_2 = self.canvas.create_image(
            223.0,
            84.0,
            image=image_image_2
        )

        self.canvas.create_text(
            32.0,
            308.0,
            anchor="nw",
            text="É RAPIDINHO, PROMETO!",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        self.canvas.create_text(
            787.0,
            141.0,
            anchor="nw",
            text="Qual a sua Rua?",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        entry_1 = Entry(
            self.master,
            bd=0,
            bg=pixel_color,
            fg="#000716",
            highlightthickness=0,
            font=("Arial 35")
        )
        entry_1.place(
            x=583.0,
            y=218.0,
            width=722.0,
            height=98.0
        )

        KeyboardOneEntry.create_keyboard(self.master,entry_1,on_button_click)

        self.canvas.create_rectangle(
            549.0,
            325.0,
            1334.0,
            330.0,
            fill="#000000",
            outline="")
        self.master.mainloop()
