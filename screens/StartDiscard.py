import subprocess
import tkinter as tk
from datetime import time
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import Finished_discard


class StartDiscard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def subprocesso4(self):
            # Fechando a porta de descarte
            process = subprocess.Popen(["./m2right"], stdout=subprocess.PIPE, universal_newlines=True)
            output = ""
            for line in process.stdout:
                output += line
                self.text_panel.config(text=output)
            process.wait()

        def subprocesso3(self):
            # Abrindo a porta de descarte
            process = subprocess.Popen(["./m2left"], stdout=subprocess.PIPE, universal_newlines=True)
            output = ""
            for line in process.stdout:
                output += line
                self.text_panel.config(text=output)
            process.wait()

            time.sleep(10)
            subprocesso4(self)

        def on_button_click():
            # subprocesso3(self)
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Finished_discard.Finished_discard(master)

        def restart_app(self):
            from screens.Home import Home
            home = Home(master)
        def cancel():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
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
            550.0,
            128.0,
            anchor="nw",
            text="Descartar itens",
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
            553.0,
            233.0,
            anchor="nw",
            text="INSIRA OS PRODUTOS NA ABERTURA\nCENTRAL DO COLETOR.",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        cancel_and_exit_button = PhotoImage(
            file=relative_to_assets("cancel_and_exit_button.png"))
        button_1 = Button(
            self.master,
            image=cancel_and_exit_button,
            borderwidth=0,
            highlightthickness=0,
            command=cancel,
            relief="flat"
        )
        button_1.place(
            x=736.0,
            y=598.0,
            width=600.0,
            height=105.35211181640625
        )

        open_colector_button = PhotoImage(
            file=relative_to_assets("open_colector.png"))
        button_2 = Button(
            self.master,
            image=open_colector_button,
            borderwidth=0,
            highlightthickness=0,
            command=on_button_click,
            relief="flat"
        )
        button_2.place(
            x=32.0,
            y=598.0,
            width=600.0,
            height=105.35211181640625
        )

        down_arrow_icon = PhotoImage(
            file=relative_to_assets("down_arrow_icon.png"))
        image_3 = canvas.create_image(
            350.0,
            318.0,
            image=down_arrow_icon
        )

        canvas.create_text(
            550.0,
            360.0,
            anchor="nw",
            text="O TEMPO PARA VOCÊ INSERIR OS PRODUTOS\nNO COLETOR É DE 30 SEGUNDOS",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )
        self.master.mainloop()
