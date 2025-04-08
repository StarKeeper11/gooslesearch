import sqlitecloud

try:
    conn = sqlitecloud.connect("sqlitecloud://cdwkovcahz.g6.sqlite.cloud:8860/goosle?apikey=jPOcAQ1fGUqluIsAUbpEKtMjrPfZxxz3yg8V2IGTEIk")
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")