import json
import re

from Constants import DATA_MASTER_FILE


def validar_email(email):
    padrao = r"^[a-zA-Z0-9_.+-]{3,}@[a-zA-Z0-9-]{3,}\.[a-zA-Z0-9-.]{2,}$"
    if re.match(padrao, email):
        return True
    else:
        return False
def verificar_email(entry_1, lbl_resultado):
    email = entry_1.get()
    if validar_email(email):
        lbl_resultado.config(text="Email válido!")
    else:
        lbl_resultado.config(text="Email inválido!")
def verificar_email_registro(email):
    email = email
    if validar_email(email):
        return True
    else:
        return False

def is_email_registered(DATA_MASTER_FILE, email):
    email = email
    with open(DATA_MASTER_FILE, 'r') as f:
        for line in f:
            d = json.loads(line)
            if email in d.values():
                return True
    return False