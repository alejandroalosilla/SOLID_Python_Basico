"""
Exercicio 4: Escreva uma função que recebe um objeto de coleção
e retorna o valor do maior número dentro dessa coleção
faça outra função que retorna o menor número dessa coleção
"""


def maior_da_lista(lista):
    maior_valor = max(lista)
    return maior_valor


def menor_da_lista(lista):
    menor_valor = min(lista)
    return menor_valor


lista_de_numeros = []

contador = 1
while contador <= 20:
    try:
        numero_int = int(input('Digite um número inteiro: '))
        lista_de_numeros.append(numero_int)
        contador += 1
    except ValueError:
        print('Por favor, digita um número do tipo inteiro!')

print(f'O maior valor da lista: {maior_da_lista(lista_de_numeros)}')
print(f'O menor valor da lista: {menor_da_lista(lista_de_numeros)}')
