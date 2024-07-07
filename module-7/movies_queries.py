import mysql.connector

# Database Configuration
config = {
    'user': 'root',
    'password': 'D40031132!',
    'host': '127.0.0.1',  
    'database': 'movies'
}

# Connection
try:
    cnx = mysql.connector.connect(**config)
    print("Connected to MySQL!")
except mysql.connector.Error as err:
    print(f"Failed to connect: {err}")

cursor = cnx.cursor()

# Query 1: Select all fields from the 'studio' table (no changes needed)
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
print("\n--- Studios ---")
for studio in studios:
    print(studio)

# Query 2: Select all fields from the 'genre' table (no changes needed)
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
print("\n--- Genres ---")
for genre in genres:
    print(genre)

# Query 3: Select movie names with runtime < 2 hours
cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")  # Using 'film_runtime'
short_films = cursor.fetchall()
print("\n--- Short Films (< 2 hours) ---")
for film in short_films:
    print(film[0])  # Access the film name

# Query 4: Group film names and directors by director (no changes needed)
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")  # Using 'film_name' and 'film_director'
films_by_director = cursor.fetchall()
print("\n--- Films Grouped by Director ---")
current_director = None
for film, director in films_by_director:
    if director != current_director:
        print(f"\n{director}:")
        current_director = director
    print(f"  - {film}")

# Close the connection
cnx.close()
