"""
Exercicio 3: Faça um programa que leia a quantidade de pessoas que
serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e
colocar em uma lista de convidados.
Após isso irá imprimir todos os nomes da lista.
"""

while True:
    try:
        quantidade_de_pessoas = int(input('Quantidade de pessoas convidadas: '))
        break
    except ValueError:
        print('Por favor, digite um número inteiro.')

lista_de_pessoas = []
c = 1

while c <= quantidade_de_pessoas:
    nome_da_pessoa = input(f'Digite o nome da {c}º pessoa: ').strip().capitalize()
    lista_de_pessoas.append(nome_da_pessoa)
    c += 1

print('\nLista de pessoas: ')
for i, nome in enumerate(lista_de_pessoas):
    print(f'{i+1}º nome: {nome}')
