listadevalores = []
listaseparado = []
dicpedidos = {}
i = 0

clientes = int(input())
itens = int(input())

while True:
    pedidos = str(input())
    dicio = {str(pedidos.split(' ')[0]):int(pedidos.split()[-1])}
    dicpedidos.update(dicio)
    i = i + 1
    if i == itens:
        break

reserva = str(input())
listadereserva = reserva.split(',')

for chave, valor in dicpedidos.items():
    for pr in listadereserva:
        if pr in chave:
            listaseparado.append(valor)
            listadevalores.append(valor)
        else:
            listadevalores.append(valor)

print(sum(set(listadevalores)))
print(int(sum(set(listadevalores)) / clientes))
print(sum(listaseparado))