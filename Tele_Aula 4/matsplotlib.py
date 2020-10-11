import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

Data = {'Ano' : [1938, 1948, 1958, 1968, 1978, 1988, 1998, 2008, 2018 ],
        'Taxa_Desemprego': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 5.5, 6.3]
        }

df = pd.Dataframe(Data, columns=['Ano', 'Taxa_Desemprego'])

df.plot(x='Ano', y='Taxa_Desemprego', kind='line') # Criação do gráfico eixo X e Y, tipo dgráfico,'Line'
plt.show() # Funcionalidade para mostrar o gráfico

df.splot.scatter(x='Ano', y='Taxa_Desemprego')
plt.show()