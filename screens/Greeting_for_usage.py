import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

from Constants import OUTPUT_PATH, ASSETS_PATH

class Greeting_for_usage(tk.Frame):
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
            restart_app(self)

        def restart_app(self):
            from screens.Home import Home
            home = Home(master)

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
            53.0,
            196.0,
            anchor="nw",
            text="Obrigado!",
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
            53.0,
            269.0,
            anchor="nw",
            text="SUA AÇÃO AJUDARÁ\nCRIANÇAS DE TODO O BRASIL!",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("finish_usage_button.png"))
        button_2 = Button(
            self.master,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=on_button_click,
            relief="flat"
        )
        button_2.place(
            x=32.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        canvas.create_text(
            53.0,
            380.0,
            anchor="nw",
            text="O PROPÓSITO DA ECO SAVER É \nAJUDAR A COMBATER A FOME NO BRASIL, \nE CADA ITEM RECICLADO CONTA!",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            736.0,
            77.0,
            anchor="nw",
            text="CONHEÇA MAIS SOBRE A NOSSA AÇÃO",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            736.0,
            128.0,
            anchor="nw",
            text="APONTANDO A CAMERA DO SEU \nCELULAR PARA O QR CODE ABAIXO",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_rectangle(
            875.0,
            232.0,
            1197.0,
            554.0,
            fill="#FFFFFF",
            outline="")
        
        self.master.mainloop()
