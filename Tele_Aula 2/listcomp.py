linguagens = ['Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin']
print('Antes da listcomp = ',linguagens)
linguagens_C = [item for item in linguagens if 'C' in item]
print('\n',linguagens_C)