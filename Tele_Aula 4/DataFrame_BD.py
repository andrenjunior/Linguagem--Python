import pandas as pd 
import sqlite3

conector = sqlite3.connect('conta.db')
df = pd.read_sql_query('Select * From cadastro', conector)
print(df.head())

# Criação de uma coluna no DB 

data = pd.DataFrame([[200, 'blusa', 59.9], [191, 'calça', 89.9], [283, 'camisa', 99.9]],
                    columns = ['id', 'descricao', 'valor'] ) 

data.to_sql('Produto', conector)  # Irá gravar no BD os dados e o nome da Tabela 

data = pd.read_sql_query('Select * From Produto', conector)