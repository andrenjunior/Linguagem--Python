# import mysql.connector

host = 'XXXXX'
port = 'XXXXX'
database = 'XXXXX'
username = 'XXXXX'
password = 'XXXXX'

conn_str = fr"host={host}, user={username}, passwd={password}, database={database}"
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")

query = "select * from XXX.YYYY"
df = pd.read_sql(query, conn)