"""
Calcular o dobro de um numero e continuar S ou N (else)
"""
import os
os.system('cls')

opcao = 's'
qtd = 0

while opcao == 's' or opcao == 'S':

    num = float(input('Número: '))
    dobro = num * 2
    print(f'O dobro de {num} é {dobro}')

    opcao = input('Continuar, [s]im o [n]ão? ')
    qtd += 1

else: # Se o laço terminar sem interrupção
    print(f'Você calculou {qtd} vezes!')

