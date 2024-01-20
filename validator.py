import re # Importa a biblioteca re

def validate(cpf_input):# Define uma função para validar um CPF usando uma expressão regular e uma função lambda
    pattern = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$" # Verifica se o CPF tem o formato correto usando uma expressão regular
    if not re.match(pattern, cpf_input):
        return False

    cpf = cpf_input.replace(".", "").replace("-", "")# Remove os pontos e o traço do CPF
    cpf = list(map(int, cpf)) # Converte o CPF em uma lista de inteiros

    def calculate_digit(cpf, weight):# Calcula o dígito verificador usando uma função lambda
        return (sum(a * b for a, b in zip(cpf, weight)) * 10) % 11
    weight_first = list(range(10, 1, -1))# Define os pesos para o primeiro e o segundo dígito
    weight_second = list(range(11, 1, -1))

    # Compara os dígitos verificadores com os dígitos fornecidos
    if calculate_digit(cpf, weight_first) == cpf[9] and calculate_digit(cpf, weight_second) == cpf[10]:
        return True
    else:
        return False
