import pymysql

# Database connection details
HOST = "mysqldb"
USER = "root"
PASSWORD = "root"
DATABASE = "techgeekconnect"

# Establish a connection to MySQL
conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usernames (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
""")

# Insert data into the table
user_name = input("Enter your name: ")
cursor.execute("INSERT INTO usernames (name) VALUES (%s)", (user_name,))
conn.commit()  # Save changes

print("\nData inserted successfully!\n")

# Read and display data from the database
cursor.execute("SELECT name FROM usernames")
rows = cursor.fetchall()

print("Stored Names in Database:")
for row in rows:
    print(row[0])

# Close the cursor and connection
cursor.close()
conn.close()
