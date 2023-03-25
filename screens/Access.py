import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import Login, Username

class Acess(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def open_login_window():
            print("Pressionado")
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Login.Login(master)

        def open_create_username_window():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Username.Username(master)

        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = self.canvas.create_image(
            683.0,
            384.0,
            image=image_image_1
        )

        self.canvas.create_text(
            362.0,
            276.0,
            anchor="nw",
            text="Você já possui conta?",
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

        create_account_button = PhotoImage(
            file=relative_to_assets("create_account_button.png"))
        button_1 = Button(
            self.master,
            image=create_account_button,
            borderwidth=0,
            highlightthickness=0,
            command=open_create_username_window,
            relief="flat"
        )
        button_1.place(
            x=721.0,
            y=483.0,
            width=600.0,
            height=105.35211181640625
        )

        access_account = PhotoImage(
            file=relative_to_assets("access_account_button.png"))
        button_2 = Button(
            self.master,
            image=access_account,
            borderwidth=0,
            highlightthickness=0,
            command=open_login_window,
            relief="flat"
        )
        button_2.place(
            x=46.0,
            y=483.0,
            width=600.0,
            height=105.35211181640625
        )
        self.master.mainloop()