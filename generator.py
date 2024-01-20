from validator import validate # Importa a função validate do validador.py
import random # Importa a biblioteca random

#cpf = input("Digite o CPF: ")# Pede ao cliente para digitar o CPF
#print("O CPF digitado foi:", cpf) # Mostra o CPF na tela
#print("Um CPF gerado foi:",# Imprime um CPF gerado
# generate())

def generate():# Define uma função para gerar um CPF aleatório e válido
    while True:
        cpf = [random.randint(0, 9) for i in range(11)]# Gera uma lista de 11 números aleatórios entre 0 e 9
     ## print(cpf)
        cpf_txt = "".join(map(str, cpf))# Converte a lista em uma string
     ## print(cpf_txt)
        if validate(cpf_txt): # Verifica se o CPF é válido usando a função validate
           ## return f"{cpf_txt[:3]}.{cpf_txt[3:6]}.{cpf_txt[6:9]}-{cpf_txt[9:]}" # Retorna o CPF no formato xxx.xxx.xxx-xx
           ## return cpf_txt
            break

print(generate())