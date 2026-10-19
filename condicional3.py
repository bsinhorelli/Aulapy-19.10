"""
'pós condicional'
"""
import os
os.system('cls')

qtd = 0

while True:
    
    num = float(input('Número: '))
    dobro = num * 2
    print(f'O dobro de {num} é {dobro}')

    opcao = input('Continuar, [s]im o [n]ão? ')
    qtd += 1

else: # Se o laço terminar sem interrupção
    print(f'Você calculou {qtd} vezes!')

