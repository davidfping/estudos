from random import choice
jogada = str(input('Escolha  pedra, papel ou tesoura: '))
jogadas = ['pedra', 'papel', 'tesoura']
maquina = choice(jogadas)

if 'pedra' in maquina and 'pedra' in jogada:
    print(f'Vc Embatou: a maquina escolheu {maquina} e vc {jogada}')
elif 'pedra' in maquina and 'papel' in jogada:
    print(f'Vc perdeu: a maquina esclheu {maquina} e vc {jogada}')
elif 'pedra' in maquina and 'tesoura' in jogada:
    print(f'Vc Ganhou: a maquina escolheu {maquina} e vc {jogada}')

if 'papel' in maquina and 'pedra' in jogada:
    print(f'Vc Ganhou: a maquina escolheu {maquina} e vc {jogada}')
elif 'papel' in maquina and 'papel' in jogada:
    print(f'Vc Embatou: a maquina escolheu {maquina} e vc {jogada}')
elif 'papel' in maquina and 'tesoura' in jogada:
    print(f'Vc Perdeu: a maquina escolheu {maquina} e vc {jogada}')

if 'tesoura' in maquina and 'pedra' in jogada:
    print(f'Vc Ganhou: a maquina escolheu {maquina} e vc {jogada}')
elif 'tesoura' in maquina and 'papel' in jogada:
    print(f'Vc Perdeu: a maquina escolheu {maquina} e vc {jogada}')
elif 'tesoura' in maquina and 'tesoura' in jogada:
    print(f'Vc Embatou: a maquina escolheu {maquina} e vc {jogada}')