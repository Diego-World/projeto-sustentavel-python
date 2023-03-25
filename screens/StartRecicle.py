import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import Scan_bar_code


class StartRecicle(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def on_button_click():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Scan_bar_code.Scan_bar_code(master)

        def restart_app(self):
            from screens.Home import Home
            home = Home(master)
        def cancel():
            restart_app(self)

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
        background = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = canvas.create_image(
            683.0,
            384.0,
            image=background
        )

        canvas.create_text(
            66.0,
            166.0,
            anchor="nw",
            text="Vamos começar a incluir os itens",
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
            298.0,
            336.0,
            anchor="nw",
            text="APONTE O\n CÓDIGO DE\n BARRAS\n PARA O LEITOR\n",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        start_recycle_button = PhotoImage(
            file=relative_to_assets("start_recycle_button.png"))
        button_1 = Button(
            self.master,
            image=start_recycle_button,
            borderwidth=0,
            highlightthickness=0,
            command=on_button_click,
            relief="flat"
        )
        button_1.place(
            x=736.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        cancel_button = PhotoImage(
            file=relative_to_assets("cancel_button.png"))
        button_2 = Button(
            self.master,
            image=cancel_button,
            borderwidth=0,
            highlightthickness=0,
            command=cancel,
            relief="flat"
        )
        button_2.place(
            x=32.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        canvas.create_text(
            230.0,
            336.0,
            anchor="nw",
            text="01",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            539.0,
            336.0,
            anchor="nw",
            text="02",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            608.0,
            336.0,
            anchor="nw",
            text="INSIRA O\n ITEM NO\n COLETOR",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            821.0,
            351.0,
            anchor="nw",
            text="03\n",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            882.0,
            336.0,
            anchor="nw",
            text="REPITA O\n PROCESSO\n ATÉ O FIM\n DOS ITENS",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )
        self.master.mainloop()
