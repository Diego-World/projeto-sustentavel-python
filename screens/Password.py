import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import AccountCreated


class Password(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def create_account():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            AccountCreated.AccountCreated(master)

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
            486.0,
            243.0,
            anchor="nw",
            text="Senha de acesso",
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
            text="Foi encaminhado para o seu e-mail uma senha aleatória.",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        generate_account_button = PhotoImage(
            file=relative_to_assets("generate_account_button.png"))
        button_1 = Button(
            self.master,
            image=generate_account_button,
            borderwidth=0,
            highlightthickness=0,
            command=create_account,
            relief="flat"
        )
        button_1.place(
            x=383.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        password_icon = PhotoImage(
            file=relative_to_assets("password_icon.png"))
        image_3 = canvas.create_image(
            350.0,
            318.0,
            image=password_icon
        )

        canvas.create_text(
            486.0,
            399.0,
            anchor="nw",
            text="Não se preocupe, será possível alterar posteriormente.",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )
        self.master.mainloop()
