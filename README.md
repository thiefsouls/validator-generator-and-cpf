Documentação do código

Este projeto contém 3 arquivos Python:

generator.py: gerador de CPFs aleatórios e válidos
validator.py: validador de CPFs
cpf.py: Gerador de CPFs

A função generate() do arquivo generator.py gera CPFs aleatórios e válidos. A função funciona da seguinte forma:

Gera uma lista de 11 números aleatórios entre 0 e 9.
Converte a lista em uma string.
Verifica se o CPF é válido usando a função validate().
Se o CPF for válido, a função o retorna no formato xxx.xxx.xxx-xx.
Validador de CPFs

A função validate() do arquivo validator.py valida CPFs. A função funciona da seguinte forma:

Verifica se o CPF tem o formato correto usando uma expressão regular.
Remove os pontos e o traço do CPF.
Converte o CPF em uma lista de inteiros.
Calcula os dígitos verificadores usando uma fórmula matemática.
Compara os dígitos verificadores calculados com os dígitos fornecidos.
Se os dois forem iguais, o CPF é válido.

Exemplo de uso isso já esta no cpf.py

Aqui está um exemplo de como usar o código:

import generator
import validator

cpf = generator.generate()
is_valid = validator.validate(cpf)

print(cpf)
print(is_valid)

Sugestões de melhoria

Aqui estão algumas sugestões de melhoria para o código:

O validador poderia ser otimizado usando uma fórmula matemática para calcular os dígitos verificadores.
O gerador poderia ser otimizado usando uma técnica de geração de números pseudoaleatórios mais eficiente.

Contribuições
Contribuições são bem-vindas. Por favor, abra um pull request no GitHub se você tiver alguma melhoria ou correção para o código.
