import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import Add_more_item_or_finish


class Start_Discard_for_recycle(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def add_more_item_or_finish():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Add_more_item_or_finish.Add_more_item_or_finish(master)

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
            384.0,
            image=image_image_1
        )

        canvas.create_text(
            486.0,
            239.0,
            anchor="nw",
            text="DESCARTE O ITEM",
            fill="#000000",
            font=("Aldrich Regular", 60 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("logo_recicla_machine.png"))
        image_2 = canvas.create_image(
            223.0,
            84.0,
            image=image_image_2
        )

        canvas.create_text(
            486.0,
            320.0,
            anchor="nw",
            text="AO ABRIR O COLETOR",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("done_button.png"))
        button_1 = Button(
            self.master,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=add_more_item_or_finish,
            relief="flat"
        )
        button_1.place(
            x=383.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("down_arrow_icon.png"))
        image_3 = canvas.create_image(
            350.0,
            318.0,
            image=image_image_3
        )
        self.master.mainloop()
