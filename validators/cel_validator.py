import re

def validar_celular(cel):
    cel = extrair_numero_telefone(cel)
    if len(cel) == 11:
        return True
    else:
        return False

def formata_cel(cel):
    return f'({cel[:2]}) {cel[2:7]}-{cel[7:]}'

def verificar_celular(cel):
    cel = cel
    if validar_celular(cel):
        cel = formata_cel(cel)
    return cel

def extrair_numero_telefone(cel):
    numero = re.sub(r'\D', '', cel)
    return numero

def verificar_celular_registro(cel):
    cel = cel
    if validar_celular(cel):
        return True
    else:
        return False