import sqlitecloud

# Open the connection to SQLite Cloud
conn = sqlitecloud.connect("sqlitecloud://cdwkovcahz.g6.sqlite.cloud:8860/goosle?apikey=nxRer9T2lsUNVidI13DbH7nY5qhIJ07VWyU3OmE6hxs")
cursor = conn.execute('SELECT * FROM users')
result = cursor.fetchone()

print(result)

conn.close()