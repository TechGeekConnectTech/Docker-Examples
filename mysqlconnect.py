import pymysql

HOST="mysqldb"
USER="root"
PASSWORD="root"
DATABASE="techgeekconnect"

conn = pymysql.connect(host=HOST,user=USER,password=PASSWORD,database=DATABASE)
cursor=conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usernames(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    )
""")

user_name=input("Enter User Name :")
cursor.execute("INSERT INTO usernames (name) VALUES (%s)",(user_name,))
conn.commit()
print("\n Data Inserted Successfully")

cursor.execute("SELECT name FROM usernames")
rows=cursor.fetchall()

print("\n This Values are Aviable into Database")
for row in rows:
    print(row[0])

cursor.close()
conn.close()

