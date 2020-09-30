def binary_search (array, item, inicio=0, fim=None):
    if fim is None:
        fim = len(array)-1
    if inicio <= fim:
        m = (inicio + fim)//2  # Divisão inteira
        if array[m] == item:
            return m
        if item < array[m]:
            return  binary_search(array, item, inicio, m-1)   
        else:
            return  binary_search(array, item, m+1, fim)
    return None
    lista = [2, 3, 4]     
    binary_search(lista, 4,)  
    print(lista)     