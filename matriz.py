def matriz_con(linhas, colunas, valores):
    lista = []
    for i in range(linhas):
        lista.append(0 * [linhas])
    contador = 0
    while True:
        if len(lista[contador]) < colunas:
            lista[contador].append(valores)
        else:
            contador = contador + 1
        if contador == linhas:
            break
    return lista


def matriz_des(linhas, colunas):
    """
    :param linhas: Determina o numero de linhas que tera a matriz
    :param colunas: Determina o numero de colunas que tera a matriz
    :return: retorna uma matriz LinhaXColuna
    Pergunta o valor que sera colocado em cada ponto da matriz
    """
    lista = []
    for i in range(linhas):
        lista.append(0 * [linhas])
    contador = 0
    while True:
        if len(lista[contador]) < colunas:
            valores = input(f'Digite um valor para a linha {contador}')
            lista[contador].append(valores)
        else:
            contador = contador + 1
        if contador == linhas:
            break
    return lista

def matriz_fibonacci(linhas, colunas, n1=0, n2=1):
    """

    :param linhas: Determina o numero de linhas que tera a matriz
    :param colunas: Determina o numero de colunas que tera a matriz
    :return: Uma Matriz de Fibonacci
    """
    lista = []
    for i in range(linhas):
        lista.append(0 * [linhas])
    contador = 0
    while True:
        if len(lista[contador]) < colunas:
            lista[contador].append(n1)
            nx = n1 + n2
            n1 = n2
            n2 = nx
        else:
            contador = contador + 1
        if contador == linhas:
            break
    return lista