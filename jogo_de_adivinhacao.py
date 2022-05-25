from time import sleep
from random import randint, choice

print('='*45)
print(f"{'VAMOS JOGAR UM JOGO DE ADIVINHAÇÃO':^45}")
print('='*45)
sleep(1)

frases_perdedor = ('ARGH! Perdi.\nNa próxima eu acerto.', 'OH NÃO, eu errei.\nVocê ganhou de mim APENAS desta vez!',
                   'PFF, você é muito bom nisso!\nEspero acertar na próxima!')
frases_ganhador = ('HAHA, eu acertei!\nSou muito bom mesmo, na próxima escolha um valor mais difícil.', 'IRRUUL, acertei!\nJá te disse que sou o melhor computador?',
                   'VIVA!\nNunca duvide das minhas habilidades de computador!')
jogador = int(input(f"{'Digite um valor inteiro de 0 a 10: ':^45}"))
while jogador < 0 or jogador > 10:
    jogador = int(input(f"{'Digite um valor inteiro de 0 a 10: ':^45}"))
computador = randint(0,10)
print(f"{'O computador terá que adivinhar o valor escolhido!':^45}")
sleep(1)
print('='*45)
print(f"{'PENSANDO...':^45}")
print('='*45)
sleep(1)
print(f'Acho que o valor que você escolheu foi {computador}!')
sleep(1)
if computador != jogador:
    print(choice(frases_perdedor))
else:
    print(choice(frases_ganhador))
