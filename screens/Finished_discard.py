import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
from Constants import OUTPUT_PATH, ASSETS_PATH
from screens import Greeting_for_usage

class Finished_discard(tk.Frame):
    def __init__(self, master):
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
            Greeting_for_usage.Greeting_for_usage(master)

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
        image_image_1 = PhotoImage(
            file=relative_to_assets("background.png"))
        image_1 = canvas.create_image(
            683.0,
            384.0,
            image=image_image_1
        )

        canvas.create_text(
            550.0,
            128.0,
            anchor="nw",
            text="Terminou?",
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
            550.0,
            257.0,
            anchor="nw",
            text="CLIQUE NO BOTÃO \nABAIXO QUANDO TERMINAR \nDE INSERIR OS PRODUTOS \nNO COLETOR",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("cancel_and_exit_button.png"))
        button_1 = Button(
            self.master,
            image=button_image_1,
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

        button_image_2 = PhotoImage(
            file=relative_to_assets("already_finished_button.png"))
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
            y=598.0,
            width=600.0,
            height=105.35211181640625
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("confirm_creation_icon.png"))
        image_3 = canvas.create_image(
            375.0,
            344.0,
            image=image_image_3
        )
        self.master.mainloop()