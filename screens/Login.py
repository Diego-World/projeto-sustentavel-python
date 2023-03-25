import json
import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage, messagebox

from Constants import ASSETS_PATH, OUTPUT_PATH
from Constants import DATA_STAGE_LOGIN_FILE
from StageLoginHelper import copy_login_data_stage_to_master
from keyboard import KeyboardTwoEntry
from screens import Menu


class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        bg_image = PhotoImage(file=relative_to_assets('background.png'))
        pixel_color = "#" + "".join(map(lambda x: hex(x)[2:].zfill(2), bg_image.get(50, 100)))

        def save_Login():
            username = entry_1.get()
            password = entry_2.get()

            if username == "" or password == "":
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            else:
                try:
                    with open(DATA_STAGE_LOGIN_FILE, "r") as f:
                        data = json.load(f)
                except:
                    data = []

                dic = {
                    "username": username,
                    "password": password
                }
                with open(DATA_STAGE_LOGIN_FILE, "w") as f:
                    f.write(json.dumps(dic))

        def destroy_call():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Menu.Menu(master)
        def save_login_data():
            save_Login()
            copy_login_data_stage_to_master()
            destroy_call()

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
        background = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = self.canvas.create_image(
            683.0,
            384.0,
            image=background
        )

        self.canvas.create_text(
            58.0,
            202.0,
            anchor="nw",
            text="Informe seus\ndados para \nacessar sua conta",
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
            826.0,
            11.0,
            anchor="nw",
            text="email ou CPF",
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
            x=615.0,
            y=75.0,
            width=667.0,
            height=98.0,
        )

        entry_2 = Entry(
            self.master,
            bd=0,
            bg=pixel_color,
            fg="#000716",
            highlightthickness=0,
            font=("Arial 35"),
            show="*"
        )
        entry_2.place(
            x=615.0,
            y=256.0,
            width=667.0,
            height=98.0
        )

        self.canvas.create_text(
            58.0,
            202.0,
            anchor="nw",
            text="Informe seus\ndados para \nacessar sua conta",
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
            885.0,
            195.0,
            anchor="nw",
            text="Senha",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        self.canvas.create_rectangle(
            588.0,
            178.0,
            1295.0001220703125,
            183.92698669433594,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            579.0,
            359.99998474121094,
            1295.0005493164062,
            366.89892578125,
            fill="#000000",
            outline="")

        KeyboardTwoEntry.create_keyboard(self.master,entry_1,entry_2,save_login_data)

        self.master.mainloop()