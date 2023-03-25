import tkinter as tk
from tkinter import INSERT
from tkinter.font import Font as font

caps_mode = False
shift_mode = False
symbols_mode = False

def create_keyboard(window,entry_1,entry_2,function):
    allButtons = []
    DEF_WIDTG = 1366
    DEF_HEIGHT = 330

    CONTRASTCLICK_COL = "#4169E1"
    row1 = ["q+/1", "w+/2", "e+/3", "r+/4", 't+/5', 'y+/6', 'u+/7', 'i+/8', 'o+/9', 'p+/0', "Backspace"]
    row2 = ["Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", "Enter"]
    row3 = ["Shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "?"]
    row4 = ["Simbolos", "@", " ", ".com", "<=", "=>"]

    rows = [row1, row2, row3, row4]

    shiftSp = row1[0:10]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "'",
               ",", ".", "/", "`", "~"]
    specials = ["Caps", "Shift", "Simbolos", "Backspace", "Enter", "<=", "=>", " "] + symbols
    nonLetterKey = specials

    width15 = ["Caps"]
    width20 = ["<=", "=>", "Enter"]
    width25 = ["Shift", "Backspace"]
    width55 = [" "]

    def on_enter(e):
        e.widget.configure(bg="#ccc", fg="#000")
        if btnLabels[e.widget]:
            btnLabels[e.widget].configure(bg="#ccc", fg="#666")

    def on_leave(e):
        e.widget.configure(bg="#333", fg="#fff")
        if btnLabels[e.widget]:
            btnLabels[e.widget].configure(bg="#333", fg="#888")

    index = 0
    letter_to_symbol = {"q": "!", "w": "@", "e": "#", "r": "$", "t": "%", "y": "^", "u": "&", "i": "*", "o": "(",
                        "p": ")", "a": "-", "s": "_", "d": "+", "f": "=", "g": "[", "h": "]", "j": "{", "k": "}",
                        "l": ";", "z": ",", "x": ".", "c": "/", "v": "`", "b": "~", "m": "'", "n": ":"}
    switched_buttons = []

    def handleClick(event):
        global shift_mode, symbols_mode, caps_mode
        text = event.widget['text']
        if text == "Backspace":
            current_widget = window.focus_get()
            if current_widget == entry_1:
                entry_1.delete(len(entry_1.get()) - 1)
            elif current_widget == entry_2:
                entry_2.delete(len(entry_2.get()) - 1)
        elif text == "<=":
            current_widget = window.focus_get()
            if current_widget == entry_1:
                entry_1.icursor(entry_1.index(INSERT) - 1)
            elif current_widget == entry_2:
                entry_2.icursor(entry_2.index(INSERT) - 1)
        elif text == "=>":
            current_widget = window.focus_get()
            if current_widget == entry_1:
                entry_1.icursor(entry_1.index(INSERT) + 1)
            elif current_widget == entry_2:
                entry_2.icursor(entry_2.index(INSERT) + 1)
        elif text == "Enter":
            function()
            # current_widget = window.focus_get()
            # if current_widget == entry_1:
            #     entry_2.focus_set()
            # elif current_widget == entry_2:
            #     entry_1.focus_set()
        elif text == "Shift":
            shift_mode = not shift_mode
            for i, button in enumerate(row1[0:10]):
                letter, number = button.split("+/")
                if shift_mode:
                    allButtons[i].config(text=number)
                else:
                    allButtons[i].config(text=letter)
        elif text == "Caps":
            caps_mode = not caps_mode
            for button in allButtons:
                if button['text'].isalpha() and button['text'] not in specials and button['text'] != "Caps":
                    if caps_mode:
                        button.config(text=button['text'].upper())
                    else:
                        button.config(text=button['text'].lower())
        elif text == "Simbolos":
            symbols_mode = not symbols_mode
            if symbols_mode:
                for button in allButtons:
                    if button['text'] not in nonLetterKey:
                        switched_buttons.append(button)
                        button['text'] = letter_to_symbol.get(button['text'], button['text'])
            else:
                for button in switched_buttons:
                    button['text'] = next(
                        (letter for letter, symbol in letter_to_symbol.items() if symbol == button['text']),
                        button['text'])
                switched_buttons.clear()
        else:
            current_widget = window.focus_get()
            if current_widget == entry_1:
                entry_1.insert("end", text)
            elif current_widget == entry_2:
                entry_2.insert("end", text)

    # ACOMPANHA O BLOCO DE CÒDIGO ACIMA
    def symbol_on_release(event, btn):
        global index
        index = 0

    btnLabels = {}

    Y = 465

    for r in rows:
        X = 4
        for i in r:
            btnWidth = 0.079 * DEF_WIDTG
            btnHeight = 0.22 * DEF_HEIGHT

            padx = round(btnWidth / 9)
            pady = round(btnHeight / 10)

            frame = tk.Frame(window, highlightbackground="#1E1E1E", highlightthickness=4)

            if i in shiftSp:
                anchor = "se"
                labelT = i.split("+/")
                label = tk.Label(window, text=labelT[1], fg="#888", bg="#333", font=font(size=11))
                label.place(x=X + padx, y=Y + pady)
                i = labelT[0]
            else:
                anchor = "nw"
                label = None

            btn = tk.Button(frame, activebackground=CONTRASTCLICK_COL, text=i, bg="#333", fg="#fff", relief="flat",
                            padx=padx,
                            pady=pady, borderwidth=0, anchor=anchor, font=font(size=15))

            if i in width15:
                btnWidth *= 1.5
            if i in width20:
                btnWidth *= 2
            elif i in width25:
                btnWidth *= 2.5
            elif i in width55:
                btnWidth *= 5.5

            btn.place(x=0, y=0, width=btnWidth, height=btnHeight)
            frame.place(x=X, y=Y, width=btnWidth, height=btnHeight)

            X += btnWidth

            btn.bind("<Button-1>", handleClick)
            btn.bind("<ButtonRelease-1>", on_enter)
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

            btnLabels[btn] = label
            allButtons.append(btn)

        Y += btnHeight