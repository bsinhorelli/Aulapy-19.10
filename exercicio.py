import os
os.system('cls')

while True:
    nota1 = float(input('Nota: '))
    if nota1 < 0 or nota1 > 10:
        print('Erro! digite uma nota entre 0 a 10!')
        continue
    nota2 = float(input('Nota: '))
    if nota2 < 0 or nota1 > 10:
        print('Erro! digite uma nota entre 0 a 10!')
        continue

    media = (nota1 + nota2) / 2

    print(f'A media de {nota1} com {nota2} resulta {media}')

    opcao = input('Continuar, [s]im ou [n]ão? ')

    while opcao != 'S' and opcao != 's' and opcao != 'n' and opcao != 'N':
        opcao = input('ERRO! Digite S ou N: ')
    else:
        if opcao == 'n' or opcao == 'N':
            break

