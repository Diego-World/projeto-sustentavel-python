import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import Login


class AccountCreated(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def redirect_to_login():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Login.Login(master)

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
            683.0,
            288.0,
            anchor="nw",
            text="Parabéns",
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
            683.0,
            404.0,
            anchor="nw",
            text="SEU CADASTRO FOI\nCRIADO COM SUCESSO!",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        acess_account_after_creation = PhotoImage(
            file=relative_to_assets("acess_account_after_creation.png"))
        button_1 = Button(
            self.master,
            image=acess_account_after_creation,
            borderwidth=0,
            highlightthickness=0,
            command=redirect_to_login,
            relief="flat"
        )
        button_1.place(
            x=383.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        confirm_creation_icon = PhotoImage(
            file=relative_to_assets("confirm_creation_icon.png"))
        image_3 = canvas.create_image(
            514.0,
            381.0,
            image=confirm_creation_icon
        )
        self.master.mainloop()
