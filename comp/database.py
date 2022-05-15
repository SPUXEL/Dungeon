import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

        with self.connection:
            self.cursor.execute(
                    """CREATE  TABLE IF NOT EXISTS users (
                        user_id INT
                        )
                    """
                    )

    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute(
                    "INSERT INTO 'users' ('user_id') VALUES (?)",
                    (user_id,)
                    )

    def get_user(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                    "SELECT * FROM 'users' WHERE 'user_id' = ?",
                    (user_id,)).fetchall()
            return result
