"""
(Aula 2) - Variáveis, tipos, entrada, saída e operadores matemáticos.

Exercicio 1: Faça um formulário que pergunte o nome, cpf, endereço,
idade, altura e telefone e imprima isso em um relatório organizado.
"""

nome = input('Digite o nome: ').strip().capitalize()
cpf = input('Digite o CPF: ').strip()
endereco = input('Digite o endereço: ').strip()
idade = input('Digite a idade: ').strip()
altura = input('Digite sua altura: ').strip()
telefone = input('Digite seu telefone: ').strip()

formulario = {'Nome': nome, 'CPF': cpf, 'Endereço': endereco, 'Idade': idade, 'Altura': altura, 'Telefone': telefone}

print('\nFormulário:')
print(20 * '-')
for indice, dado in formulario.items():
    print(f'{indice}: {dado}')
print(20 * '-')
