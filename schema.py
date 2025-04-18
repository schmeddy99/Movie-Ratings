import sqlite3

# --------------------------------------------
# Contains all CREATE TABLE statements
# Defines the normalized database schema
# --------------------------------------------


def create_all_tables(conn):
    """
    Creates all necessary tables for the normalized movie database.
    """
    create_directors_table(conn)
    create_actors_table(conn)
    create_movies_table(conn)
    create_genres_table(conn)
    create_movie_actors_table(conn)
    create_movie_genres_table(conn)


def create_movies_table(conn):
    """
    Creates the 'movies' table.
    Stores movie-specific information and links to a director.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER,
            imdb_score REAL,
            gross INTEGER,
            duration INTEGER,
            budget INTEGER,
            content_rating TEXT,
            country TEXT,
            language TEXT,
            color TEXT,
            director_id INTEGER,
            FOREIGN KEY (director_id) REFERENCES directors(id)
        );
    """
    )


def create_directors_table(conn):
    """
    Creates the 'directors' table.
    Stores director names and Facebook likes.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS directors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            facebook_likes INTEGER
        );
    """
    )


def create_actors_table(conn):
    """
    Creates the 'actors' table.
    Stores actor names and Facebook likes.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS actors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            facebook_likes INTEGER
        );
    """
    )


def create_movie_actors_table(conn):
    """
    Creates the 'movie_actors' table.
    Defines a many-to-many relationship between movies and actors.
    Stores the actor's role order (1st, 2nd, 3rd).
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS movie_actors (
            movie_id INTEGER,
            actor_id INTEGER,
            role_order INTEGER,
            PRIMARY KEY (movie_id, actor_id),
            FOREIGN KEY (movie_id) REFERENCES movies(id),
            FOREIGN KEY (actor_id) REFERENCES actors(id)
        );
    """
    )


def create_genres_table(conn):
    """
    Creates the 'genres' table.
    Stores distinct genre names (e.g., Comedy, Action).
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    """
    )


def create_movie_genres_table(conn):
    """
    Creates the 'movie_genres' table.
    Defines a many-to-many relationship between movies and genres.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS movie_genres (
            movie_id INTEGER,
            genre_id INTEGER,
            PRIMARY KEY (movie_id, genre_id),
            FOREIGN KEY (movie_id) REFERENCES movies(id),
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        );
    """
    )
