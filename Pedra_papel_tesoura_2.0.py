from random import choice

def resolucao(maquina, humano):
    venceu = f'Voce Venceu: a jogada da maquina foi {maquina} e a sua {humano}'
    perdeu = f'Voce perdeu a maquina jogou {maquina} e vc {humano} :('
    embate = f'O jogo empatou os dois jogaram {maquina}'

    if 'papel' in maquina:
        if 'papel' in humano:
            return embate
        elif 'pedra' in humano:
            return perdeu
        elif 'tesoura' in humano:
            return venceu
    elif 'pedra' in maquina:
        if 'papel' in humano:
            return venceu
        elif 'pedra' in humano:
            return embate
        elif 'tesoura' in humano:
            return perdeu
    elif 'tesoura' in maquina:
        if 'papel' in humano:
            return perdeu
        elif 'pedra' in humano:
            return venceu
        elif 'tesoura' in humano:
            return embate

jogada = str(input('Escolha  pedra, papel ou tesoura: '))
jogadas = ['pedra', 'papel', 'tesoura']
maquina = choice(jogadas)
print(resolucao(maquina, jogada))






