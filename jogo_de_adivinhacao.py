from time import sleep
from random import randint, choice

print('==='*12)
print(' VAMOS JOGAR UM JOGO DE ADIVINHAÇÃO')
print('==='*12)
sleep(1)

frases_perdedor = ('ARGH! Perdi.\nNa próxima eu acerto.', 'OH NÃO, eu errei.\nVocê ganhou de mim APENAS desta vez!',
                   'PFF, você é muito bom nisso!\nEspero acertar na próxima!')
frases_ganhador = ('HAHA, eu acertei!\nSou muito bom mesmo, na próxima escolha um valor mais difícil.', 'IRRUUL, acertei!\nJá te disse que sou o melhor computador?',
                   'VIVA!\nNunca duvide das minhas habilidades de computador!')
jogador = int(input('Digite um valor inteiro de 0 a 10: '))
computador = randint(0,10)
print('O computador terá que adivinhar o valor escolhido!')
sleep(1)
print('=='*7)
print(' PENSANDO...')
print('=='*7)
sleep(1)
print(f'Acho que o valor que você escolheu foi {computador}!')
if computador != jogador:
    print(choice(frases_perdedor))
else:
    print(choice(frases_ganhador))