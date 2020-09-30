def valor_lista():
    for i in range(1,5):
        lista.append(int(input(f'Digite sua prova {i}: ')))

def media():
    s = 0
    for i in range(len(lista)):
        s = s + lista[i]
    m = s / 4
    return m    

lista = []
valor_lista()
m = media()
print(f'Você ficou com a média: {m}')