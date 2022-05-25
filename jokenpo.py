from random import choice
from time import sleep

print('-'*30)
print(f"{'VAMOS JOGAR JOKENPO':^30}")
print('-'*30)
sleep(1)
print(f"{'Você tem três opções.':^30}")
print(f"{'Pedra - Papel - Tesoura':^30}")
print(f"{'Escolha sabiamente!':^30}")
print('-'*30)
sleep(1)
jogador = input('Digite qual vai ser a sua jogada: [Pedra/Papel/Tesoura] ').upper().strip()
escolhas = ('PEDRA', 'PAPEL', 'TESOURA')
computador = choice(escolhas).upper()
while jogador not in escolhas:
    jogador = input('Digite qual vai ser a sua jogada: [Pedra/Papel/Tesoura] ').upper().strip()
if jogador == computador:
    print(f'PFF, SEM GRAÇA! O JOGO DEU EMPATE.\nO computador também escolheu {computador}')

elif jogador == 'PEDRA':
    if computador == 'PAPEL':
        print(f'VOCÊ PERDEU. O computador escolheu {computador}.')
    else:
        print(f'VOCÊ GANHOU! O computador escolheu {computador}.')
elif jogador == 'PAPEL':
    if computador == 'TESOURA':
        print(f'VOCÊ PERDEU. O computador escolheu {computador}.')
    else:
        print(f'VOCÊ GANHOU! O computador escolheu {computador}.')
elif jogador == 'TESOURA':
    if computador == 'PEDRA':
        print(f'VOCÊ PERDEU. O computador escolheu {computador}.')
    else:
        print(f'VOCÊ GANHOU! O computador escolheu {computador}.')
