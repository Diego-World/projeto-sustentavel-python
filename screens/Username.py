import json
import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Entry, PhotoImage, messagebox, Label
from Constants import DATA_STAGE_FILE, ASSETS_PATH, OUTPUT_PATH
from keyboard import KeyboardOneEntry
from screens import Cpf
from validators.username_validator import validar_nome

class Username(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        bg_image = PhotoImage(file=relative_to_assets('background.png'))
        pixel_color = "#" + "".join(map(lambda x: hex(x)[2:].zfill(2), bg_image.get(50, 100)))

        def on_button_click():
            username = entry_1.get()

            if username == "":
                messagebox.showerror("Erro", "Por favor, preencha o campo.")
            if validar_nome(username) == False:
                lbl_resultado.configure(text='Nome de usuário Inválido',font=("Arial 20"))
            else:
                try:
                    with open(DATA_STAGE_FILE, "r") as f:
                        data = json.load(f)
                except:
                    data = []

                dic = {}
                dic["username"] = username

                with open(DATA_STAGE_FILE, "w") as file:
                    file.write(json.dumps(dic))

                for widget in master.winfo_children():
                    widget.destroy()
                self.destroy()
                Cpf.Cpf(master)

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
            824.0,
            92.0,
            anchor="nw",
            text="Preencha primeiro",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        self.canvas.create_text(
            787.0,
            141.0,
            anchor="nw",
            text="Qual o seu nome?",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        self.canvas.create_rectangle(
            549.0,
            335.0,
            1334.0,
            330.0,
            fill="#000000",
            outline="")

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

        lbl_resultado = Label(self.master, bg=pixel_color)
        lbl_resultado.place(x=549, y=340, width=785, height=20)

        self.master.mainloop()