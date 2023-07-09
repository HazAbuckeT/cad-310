

import mysql.connector
from mysql.connector import errorcode

def show_films (cursor, title) :
    cursor.execute ("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name'\
    from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall ()

    print("\n -- {} --".format(title.title()))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

config = {
    "user": "jgruidl",
    "password": "TFJazeera1021!!",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Establish connection
    db = mysql.connector.connect(**config)
    print('\nDatabase user {} connected to MySQL on host {} with database {}'.format(config["user"], config["host"], config["database"]))

    # Create a cursor object
    cur = db.cursor()
    
    # Call show_films function
    show_films(cur, "Displaying Film Records")

    # Close the cursor and connection
    cur.close()
    db.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('The supplied username or password are invalid')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('The specified database does not exist')
    else:
        print(err)