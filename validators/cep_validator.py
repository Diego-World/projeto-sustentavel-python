import re
def validar_cep(cep):
    cep = extrair_cep(cep)
    if len(cep) == 8:
        return True
    else:
        return False
def formatar_cep(cep):
    return cep[:5] + '-' + cep[5:]
def verificar_cep(cep):
    cep = cep
    if validar_cep(cep):
        cep = formatar_cep(cep)
        return cep
def verificar_cep_registro(cep):
    cep = cep
    if validar_cep(cep):
        return True
    else:
        return False
def extrair_cep(cep):
    # Substitui todos os caracteres que não são dígitos por vazio ""
    cep = re.sub(r'\D', '', cep)
    return cep