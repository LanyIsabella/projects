from random import randint
from time import sleep

print('~'*30)
print(f"{'VAMOS JOGAR PAR OU ÍMPAR':^30}")
print('~'*30)
sleep(1)

computador_valor = randint(0, 10)
escolha = str(input(f"{'Par ou ímpar?':^30}")).upper().strip()[0]

while escolha not in 'PIÍ':
    escolha = str(input(f"{'Par ou ímpar?':^30}")).upper().strip()[0]

print('~' * 30)
valor = int(input(f"{'Digite um valor inteiro entre 0 e 10:':^30}"))
while valor < 0 or valor > 10:
    valor = int(input(f"{'Digite um valor inteiro entre 0 e 10:':^30}"))
computador_valor = randint(0,10)
valor_total = valor + computador_valor

if escolha in 'P':
    if valor_total % 2 == 0:
        print('~~~~' * 7)
        print(f'Parabéns! Você venceu.\nO computador jogou {computador_valor} e você jogou {valor}.\nO total deu {valor_total}. O valor é PAR!')
    else:
        print('~~~~' * 7)
        print(f'Não foi desta vez! O computador jogou {computador_valor} e você jogou {valor}.\nO total deu {valor_total}. O valor é ÍMPAR!')
elif escolha in 'IÍ':
    if valor_total % 2 != 0:
        print('~~~~' * 7)
        print(f'Parabéns! Você venceu.\nO computador jogou {computador_valor} e você jogou {valor}.\nO total deu {valor_total}. O valor é ÍMPAR!')
    else:
        print('~~~~' * 7)
        print(f'Não foi desta vez! O computador jogou {computador_valor} e você jogou {valor}.\nO total deu {valor_total}. O valor é PAR!')

