import re
def validar_nome(username):
    padrao = r'^[a-zA-ZÀ-ÿ]+([ \'-][a-zA-ZÀ-ÿ]+)*$'
    FORBIDEN_WORDS_FILE = ['merda', 'caralho', 'foda', 'puta', 'viado', 'cuzão']

    if re.match(padrao, username) and not any(palavra in username.lower() for palavra in FORBIDEN_WORDS_FILE):
        return True
    else:
        return False

