"""
(Aula 3) - Operadores  lógicos e estruturas de decisões (IF e ELSE).

Exercício 2: Faça um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela está apta a ser do Exército.
Para entrar no exército é preciso ter mais de 18 anos pesar
mais ou igual a 60 kilos e medir mais ou igual 1,70 metros.
"""

idade = None
peso = None
altura = None

while True:
    try:
        if idade is None:
            idade = int(input('Digite a idade: '))
        if peso is None:
            peso = float(input('Digite o seu peso: '))
        if altura is None:
            altura = float(input('Digite a altura: '))
        break
    except ValueError:
        if idade is None:
            print('Digite um valor inteiro no campo idade.')
        elif peso is None:
            print('Digite um número decimal no campo peso.')
        elif altura is None:
            print('Digite um número decimal no campo altura')

dados = {'Idade': idade, 'Peso': peso, 'Altura': altura}

print('\nDados: ')
print(20 * '-')

for indice, valor in dados.items():
    print(f'{indice}: {valor}')

print('\nStatus:')
if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Está apto a servir.')
else:
    print('Não está apto a servir')
print(20 * '-')
