import pandas as pd
import numpy as np 

df = pd.DataFrame  ({
'nome' : ['André', 'Junior', 'Nascimento'],
'idade': [38, 37, 36],
'cidade': ['RJ','SP','MG']
})

print(df)
print('\n')

vetor = np.array([5, 6, 7, 8])
v = pd.Series(vetor)

print(vetor)
print(v)
print('\n\n')
print(df.nome) # retorna somente com a coluna nome 
print('\n\n')
print(df.idade.mean()) # Retorna com a média de idade