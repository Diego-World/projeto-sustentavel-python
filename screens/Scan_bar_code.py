import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage

from Constants import ASSETS_PATH, OUTPUT_PATH
from screens import Start_Discard_for_recycle


class Scan_bar_code(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def start_discard():
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Start_Discard_for_recycle.Start_Discard_for_recycle(master)

        def start(self):
            # Espera 10 segundos antes de chamar a função start_discard
            # self.master.after(10000, start_discard)
            self.cancel_id = self.master.after(10000, start_discard)

        def restart_app(self):
            from screens.Home import Home
            home = Home(master)
        def cancel():
            if self.cancel_id is not None:
                self.master.after_cancel(self.cancel_id)
                self.cancel_id = None
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

        image_image_2 = PhotoImage(
            file=relative_to_assets("bar_code_icon.png"))
        image_2 = canvas.create_image(
            514.0,
            381.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("logo_recicla_machine.png"))
        image_3 = canvas.create_image(
            223.0,
            84.0,
            image=image_image_3
        )

        canvas.create_text(
            648.0,
            352.0,
            anchor="nw",
            text="APONTE O CÓDIGO DE BARRAS \nPARA O LEITOR",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("cancel_button.png"))
        button_1 = Button(
            self.master,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=cancel,
            relief="flat"
        )
        button_1.place(
            x=383.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        start(self)
        self.master.mainloop()
