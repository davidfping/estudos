def cifradecesar(texto, codigo=3, MODO=1):
    """

    :param texto: Texto a ser criptografado,
    :param codigo: numero para ser alterado no alphabeto (default é 3)
    :param MODO: 1 criptografar 2 decriptografa
    :return: texto
    """
    texto = texto.upper()
    alphabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto_novo = ''
    for c in texto:
        index = alphabeto.find(c)
        if index == -1:
            texto_novo += c

        else:
            if MODO == 1:
                novo_index = index + codigo
                novo_index = novo_index % len(alphabeto)
                texto_novo += alphabeto[novo_index:novo_index + 1]
            elif MODO == 2:
                novo_index = index - codigo
                novo_index = novo_index % len(alphabeto)
                texto_novo += alphabeto[novo_index:novo_index + 1]


    return texto_novo

print(cifradecesar('RLRLRLRLRL', MODO=2))

