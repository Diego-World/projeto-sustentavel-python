import tkinter as tk
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
from Constants import OUTPUT_PATH, ASSETS_PATH


class Add_more_item_or_finish(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        OUTPUT_PATH
        ASSETS_PATH

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def Scan_bar_code():
            from screens import Scan_bar_code
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Scan_bar_code.Scan_bar_code(master)

        def finish():
            from screens import Greeting_for_usage
            for widget in master.winfo_children():
                widget.destroy()
            self.destroy()
            Greeting_for_usage.Greeting_for_usage(master)

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
            328.0,
            236.0,
            anchor="nw",
            text="O que você deseja fazer?",
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

        button_image_1 = PhotoImage(
            file=relative_to_assets("finish_button.png"))
        button_1 = Button(
            self.master,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=finish,
            relief="flat"
        )
        button_1.place(
            x=733.0,
            y=417.0,
            width=600.0,
            height=105.35211181640625
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("include_item_button.png"))
        button_2 = Button(
            self.master,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=Scan_bar_code,
            relief="flat"
        )
        button_2.place(
            x=43.0,
            y=417.0,
            width=600.0,
            height=105.35211181640625
        )
        self.master.mainloop()
