# Calculadora com 6 opções de uso

# Importações
from math import sqrt
from time import sleep

# Prints para abertura do programa
print('-='*20)
print(f'{"CALCULADORA":^40}')
print('-='*20)


# Print de opções e input de escolha
sleep(1)
print(f'{"Escolha uma opção":^40}')
print('1 - Soma'
        '\n2 - Subtração'
        '\n3 - Multiplicação'
        '\n4 - Divisão'
        '\n5 - Potência'
        '\n6 - Raíz Quadrada'
        '\n7 - Sair do programa')
print('-='*20)
while True:
    escolha = int(input(f"{'Digite o valor da opção desejada: ':^40}"))
    print('-=' * 20)
    opcoes = [1, 2, 3, 4, 5, 6, 7]
    if escolha in opcoes:
        break
    print('Por favor, digite uma opção válida.')

# Condicionais para programar as opções
if escolha == 1:
    soma = 0
    # Loop para coleta de valores
    while True:
        valores =(float(input('Digite um valor: ')))
        # Operador para soma
        soma += valores
        # Loop de escolha
        while True:
            escolha = input(f"{'Você deseja continuar adicionando valores? [S/N]':^40}").upper().strip()[0]
            print('-=' * 20)
            if escolha in 'SN':
                break
            print('Por favor, digite uma opção válida.')
        if escolha == 'N':
            break
    print(f"{f'A soma dos valores digitados é de {soma}.':^40}")
if escolha == 2:
    contador = 0
    subtracao = 0
    # Loop para coleta de valores
    while True:
        valores = (float(input('Digite um valor: ')))
        # Condicional com contador para tornar a conta válida
        if contador == 0:
            subtracao = valores
        else:
            subtracao -= valores
        contador += 1
        # Loop de escolha
        while True:
            escolha = input(f"{'Você deseja continuar adicionando valores? [S/N]':^40}").upper().strip()[0]
            print('-=' * 20)
            if escolha in 'SN':
                break
            print('Por favor, digite uma opção válida.')
        if escolha == 'N':
            break
    print(f"{f'A subtração dos valores digitados é de {subtracao}.':^40}")
if escolha == 3:
    mult = 1
    # Loop para coleta de valores
    while True:
        valores = float(input('Digite um valor: '))
        # Operador para multiplicação
        mult *= valores
        # Loop de escolha
        while True:
            escolha = input(f"{'Você deseja continuar adicionando valores? [S/N]':^40}").upper().strip()[0]
            print('-=' * 20)
            if escolha in 'SN':
                break
            print('Por favor, digite uma opção válida.')
        if escolha == 'N':
            break
    print(f"{f'A multiplicação dos valores digitados é de {mult}.':^40}")
if escolha == 4:
    contador = 0
    divisao = 0
    # Loop para coleta de valores
    while True:
        valores = float(input('Digite um valor: '))
        # Condicional com contador para tornar a conta válida
        if contador == 0:
            divisao = valores
        else:
            divisao /= valores
        contador += 1
        # Loop de escolha
        while True:
            escolha = input(f"{'Você deseja continuar adicionando valores? [S/N]':^40}").upper().strip()[0]
            print('-=' * 20)
            if escolha in 'SN':
                break
            print('Por favor, digite uma opção válida.')
        if escolha == 'N':
            break
    print(f"{f'A divisão dos valores digitados é de {divisao}.':^40}")
if escolha == 5:
    # Coleta de valores + print com operador já formatado
    base = float(input('Digite o valor da base: '))
    expoente = float(input('Digite o valor do expoente: '))
    print(f"{f'A potência do valor {base} com o expoente {expoente} é {base**expoente}':^40}")
if escolha == 6:
    # Coleta de valores + print com operador formatado
    valores = float(input('Digite um valor: '))
    print(f"{f'A raíz quadrada do valor digitado é {sqrt(valores)}':^40}")
if escolha == 7:
    # prints de de saída do programa
    print(f"{'Obrigada por me utilizar.':^40}")
    print(f"{'Volte sempre!':^40}")
