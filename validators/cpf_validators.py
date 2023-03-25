import json
from validate_docbr import CPF

documento_cpf = CPF()

#Validação da Entry
def valida_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')  # Remove formatação do cpf
    if not cpf.isnumeric() or len(cpf) != 11:  # verifica se o cpf contém apenas números e possui 11 dígitos
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_verificador = (soma * 10) % 11
    if digito_verificador == 10:
        digito_verificador = 0
    if int(cpf[9]) != digito_verificador:
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_verificador = (soma * 10) % 11
    if digito_verificador == 10:
        digito_verificador = 0
    if int(cpf[10]) != digito_verificador:
        return False

    return True
def formata_cpf(cpf):
    cpf = documento_cpf.mask(cpf)
    return cpf

def verificar_cpf(cpf):
    if valida_cpf(cpf):
        cpf = formata_cpf(cpf)
        return cpf
def is_cpf_registered(DATA_MASTER_FILE, cpf):
    cpf = formata_cpf(cpf)
    with open(DATA_MASTER_FILE, 'r') as f:
        for line in f:
            d = json.loads(line)
            if cpf in d.values():
                return True
    return False