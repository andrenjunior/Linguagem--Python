def busca_sequencial (lista, elemento):
    pos = 0
    encontrado = False

    while pos < len(lista) and not encontrado:
         if lista[pos] == elemento:
             encontrado = True
         else:
             pos = pos + 1

    return encontrado

testelista = [2, 10, 8, 15, 18, 20, 1]
print(busca_sequencial(testelista, 8))
print(busca_sequencial(testelista, 21))                    
