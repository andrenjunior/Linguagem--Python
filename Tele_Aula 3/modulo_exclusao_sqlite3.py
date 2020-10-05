import sqlite3

def ExcluirCliente(cod):
    sql = 'delete from cadastro where codigo = :param'
    cursor.execute(sql, {'param': cod})
    concetor.commit()
    return  print(f'Cliente {(cod)} Excluído')




concetor = sqlite3.connect('conta.db')
cursor = concetor.cursor()

ExcluirCliente(1284)