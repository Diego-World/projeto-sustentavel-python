import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import StartDiscard, StartRecicle


class Menu(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def start_discard():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            StartDiscard.StartDiscard(master)

        def start_Recicle():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            StartRecicle.StartRecicle(master)
        def restart_app(self):
            from screens.Home import Home
            home = Home(master)
        def cancel():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            restart_app(self)

        self.canvas.place(x = 0, y = 0)
        background = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = self.canvas.create_image(
            683.0,
            384.0,
            image=background
        )

        self.canvas.create_text(
            310.0,
            276.0,
            anchor="nw",
            text="O que você deseja fazer?",
            fill="#000000",
            font=("Aldrich Regular", 64 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("logo_recicla_machine.png"))
        image_2 = self.canvas.create_image(
            278.0,
            87.0,
            image=image_image_2
        )

        descart_item_button = PhotoImage(
            file=relative_to_assets("descart_item_button.png"))
        button_1 = Button(
            self.master,
            image=descart_item_button,
            borderwidth=0,
            highlightthickness=0,
            command=start_discard,
            relief="flat"
        )
        button_1.place(
            x=729.0,
            y=384.0,
            width=600.0,
            height=105.35211181640625
        )

        recycle_button = PhotoImage(
            file=relative_to_assets("recycle_button.png"))
        button_2 = Button(
            self.master,
            image=recycle_button,
            borderwidth=0,
            highlightthickness=0,
            command=start_Recicle,
            relief="flat"
        )
        button_2.place(
            x=30.0,
            y=384.0,
            width=600.0,
            height=105.35211181640625
        )

        cancel_and_exit_button = PhotoImage(
            file=relative_to_assets("cancel_and_exit_button.png"))
        button_3 = Button(
            self.master,
            image=cancel_and_exit_button,
            borderwidth=0,
            highlightthickness=0,
            command=cancel,
            relief="flat"
        )
        button_3.place(
            x=382.0,
            y=552.0,
            width=600.0,
            height=105.35211181640625
        )
        self.master.mainloop()
