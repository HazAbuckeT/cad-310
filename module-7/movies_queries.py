# Joshua Gruidl, Module 7, 4 July 2023
# Movies Query

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "jgruidl",
    "password": "password",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print('\nDatabase user {} connected to MySQL on host {} with database {}'.format(config["user"], config["host"], config["database"]))

    # Create a cursor object
    cur = db.cursor()

    # Query 1: Select all fields from the studio table
    cur.execute("SELECT * FROM studio;")
    studio_records = cur.fetchall()
    print("\n-- DISPLAYING Studio RECORDS --")
    for row in studio_records:
        print("Studio ID: {}\nStudio Name: {}\n".format(row[0], row[1]))

    # Query 2: Select all fields from the genre table
    cur.execute("SELECT * FROM genre;")
    genre_records = cur.fetchall()
    print("\n-- DISPLAYING Genre RECORDS --")
    for row in genre_records:
        print("Genre ID: {}\nGenre Name: {}\n".format(row[0], row[1]))

    # Query 3: Select the movie names for movies with runtime less than two hours
    cur.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
    movie_records = cur.fetchall()
    print("\n-- DISPLAYING Short Film RECORDS --")
    for row in movie_records:
        print("Film Name: {}\nRuntime: {}\n".format(row[0], row[1]))

    # Query 4: Get a list of film names, and directors ordered by director
    cur.execute("SELECT film_name, film_director FROM film ORDER BY film_director;")
    film_director_records = cur.fetchall()
    print("\n-- DISPLAYING Director RECORDS in Order --")
    for row in film_director_records:
        print("Film Name: {}\nDirector: {}\n".format(row[0], row[1]))

    # Close the cursor and db connection
    cur.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(' The supplied username or password are invalid')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(' The specified database does not exist')
    else:
        print(err)


