import generator # Importa a função generator.py
import validator # Importa a função validador.py


cpf = generator.generate() # Gera um CPF aleatório e válido
is_valid = validator.validate(cpf) # Valida o CPF


print(cpf) # Imprime o CPF
print(is_valid)