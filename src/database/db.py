import sqlite3
from random import randint


class DataBase:
    def __init__(self, db_file):
        self.connect = sqlite3.connect(db_file)
        self.cursor = self.connect.cursor()

    async def add_user(self, user_name):
        with self.connect:
            return self.cursor.execute("""INSERT INTO users (user_name, rand_num) VALUES (?, ?)""",
                                       (user_name, randint(1, 100),))

    async def check_user(self, user_name):
        with self.connect:
            return bool(len(self.cursor.execute("""SELECT * FROM users WHERE user_name=(?)""",
                                                (user_name,)).fetchall()))

    async def update_name(self, user_name):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET name=(?) WHERE user_name=(?)""",
                                       ('Steve', user_name,))

    async def delete_user(self, user_name):
        with self.connect:
            return self.cursor.execute("""DELETE FROM users WHERE user_name=(?)""",
                                       (user_name,))

    async def get_rand_num(self, user_name):
        with self.connect:
            return self.cursor.execute("""SELECT rand_num FROM users WHERE user_name=(?)""",
                                       (user_name,)).fetchall()
