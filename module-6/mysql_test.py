import mysql.connector

# Database Configuration
config = {
  'user': 'root',
  'password': 'D40031132!',
  'host': '127.0.0.1',  # Usually localhost
  'database': 'movies'
}

# Connection
try:
  cnx = mysql.connector.connect(**config)
  print("Connected to MySQL!")
except mysql.connector.Error as err:
  print(f"Failed to connect: {err}")

# Close Connection (Important!)
cnx.close() 
