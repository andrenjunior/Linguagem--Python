def busca_sequencial (v, x):
    #Contador criado
    i = 0 
    #laço para percorrer o vetor
    while i < len(v):
        if v[i] == x:
            return i #Se o elemento for encontrado o return finaliza aqui
        i += 1 #Contador incrementado dentro do laço de repetição
    return -1  #Se não for encontrado o elemento o laço de repetição  para aqui.       


vetor = list(range(0,100)) # variável criada para criar a lista sequencial.
print(vetor)

posicao = busca_sequencial(vetor, 98) #Variável criada para determinar a posição do elemtno.
if posicao >= 0:
    print('O elemento foi encontrado na posição {}'.format(posicao))
else:
    print('O elemento não foi encontrado')    
