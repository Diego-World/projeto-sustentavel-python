import json
import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Text, Button, PhotoImage, END, Label,Entry
from Constants import ASSETS_PATH, OUTPUT_PATH
from Constants import DATA_STAGE_FILE
from StageHelper import copy_data_stage_to_master
from screens import Password
from validators.cel_validator import verificar_celular_registro, extrair_numero_telefone, formata_cel
from validators.cep_validator import verificar_cep_registro, extrair_cep, formatar_cep
from validators.email_validator import verificar_email_registro

class ConfirmRegister(tk.Frame):
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
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Password.Password(master)

        def verify_data_email():
            email = entry_3.get()

            if verificar_email_registro(email) == False:
                lbl_resultado.configure(text='Email Inválido',font=("Arial 20"))
                return False
            else:
                try:
                    with open(DATA_STAGE_FILE, "r") as stageData:
                        data = json.load(stageData)
                except:
                    data = [],

                data["email"] = email.rstrip()

                with open(DATA_STAGE_FILE, "w") as f:
                    f.write(json.dumps(data))

                print("Alteração de Email " + str(data))
                return True

        def verify_data_cel():
            cel = entry_4.get()

            if verificar_celular_registro(cel) == False:
                lbl_resultado.configure(text='Celular Inválido',font=("Arial 20"))
                return False
            else:
                try:
                    with open(DATA_STAGE_FILE, "r") as stageData:
                        data = json.load(stageData)
                except:
                    data = [],

                data["cel"] = cel.rstrip()

                with open(DATA_STAGE_FILE, "w") as f:
                    f.write(json.dumps(data))

                print("Alteração de cel " + str(data))
                return True

        def confirm_data():
            if verify_data_email() == True and verify_data_cel():
                copy_data_stage_to_master()
                on_button_click()
            else:
                pass

        def bring_account_information():
            with open(DATA_STAGE_FILE, "r") as stageData:
                data = json.load(stageData)
                print(str(data))

            entry_1.configure(text=data["username"])
            entry_2.configure(text=data["cpf"])
            entry_3.insert(END,data["email"])
            entry_4.insert(END,data["cel"])

        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = self.canvas.create_image(
            683.0,
            384.0,
            image=image_image_1
        )

        confirm_data_button = PhotoImage(
            file=relative_to_assets("confirm_data_button.png"))
        button_1 = Button(
            self.master,
            image=confirm_data_button,
            borderwidth=0,
            highlightthickness=0,
            command=confirm_data,
            relief="flat"
        )
        button_1.place(
            x=383.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        self.canvas.create_text(
            32.0,
            242.0,
            anchor="nw",
            text="Perfeito!",
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
            text="Agora, por favor ",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        self.canvas.create_text(
            646.0,
            25.0,
            anchor="nw",
            text="Nome",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        self.canvas.create_text(
            32.0,
            350.0,
            anchor="nw",
            text="CONFIRA SEUS DADOS",
            fill="#000000",
            font=("Aldrich Regular", 24 * -1)
        )

        self.canvas.create_text(
            646.0,
            110.0,
            anchor="nw",
            text="CPF",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        self.canvas.create_text(
            646.0,
            195.0,
            anchor="nw",
            text="email",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        self.canvas.create_text(
            646.0,
            280.0,
            anchor="nw",
            text="Celular",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("show_data_entry_background_image.png"))
        entry_1 = Label(
            self.master,
            bg=pixel_color,
            fg="#000716",
            font=("Arial 30")
        )

        entry_1.place(
            x=796.0,
            y=25.0,
            width=503.0,
            height=47.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("show_data_entry_background_image.png"))
        entry_2 = Label(
            self.master,
            bg=pixel_color,
            fg="#000716",
            font=("Arial 30"),
            highlightthickness=0,
            bd=0
        )
        entry_2.place(
            x=796.0,
            y=110.0,
            width=503.0,
            height=47.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("show_data_entry_background_image.png"))
        entry_3 = Entry(
            self.master,
            bg=pixel_color,
            fg="#000716",
            font=("Arial 30"),
            highlightthickness = 0,
            bd = 0
        )
        entry_3.place(
            x=796.0,
            y=195.0,
            width=503.0,
            height=47.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("show_data_entry_background_image.png"))
        entry_4 = Entry(
            self.master,
            bg=pixel_color,
            fg="#000716",
            font=("Arial 30"),
            highlightthickness=0,
            bd=0
        )
        entry_4.place(
            x=796.0,
            y=280.0,
            width=503.0,
            height=47.0
        )

        bring_account_information()

        lbl_resultado = Label(self.master, bg=pixel_color)
        lbl_resultado.place(x=780, y=330, width=450, height=40)

        self.master.mainloop()
