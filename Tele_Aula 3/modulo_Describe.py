# Só é preciso importar a biblioteca uma vez. Importamos novamente para manter todo o código em uma única célula
import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

# Lista as tabelas do banco de dados
cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")
print('Tabelas:')
for tabela in cursor.fetchall():
    print(tabela)

# Captura a DDL usada para criar a tabela
tabela = 'fornecedor'
cursor.execute(f"""SELECT sql FROM sqlite_master WHERE type='table' AND name='{tabela}'""")
print(f'\nDDL da tabela {tabela}:')
for schema in cursor.fetchall():
    print("%s" % (schema))
    
cursor.close()
conn.close()