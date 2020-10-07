import pandas as pd
import numpy as np 

df = pd.DataFrame  ({
'nome' : ['André', 'Junior', 'Nascimento'],
'Idade': [38, 37, 36],
'cidade': ['RJ','SP','MG']
})

print(df)
print('\n')

vetor = np.array([5, 6, 7, 8])
v = pd.Series(vetor)

print(vetor)
print(v)