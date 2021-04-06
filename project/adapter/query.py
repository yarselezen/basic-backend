from typing import List

from project.domain.model import User
from project.domain.query import UserQueries
from project.lib.db_pool import DbConnectionPool


class DbUserQueries(UserQueries):
    def __init__(self, connection_pool: DbConnectionPool):
        self.connection_pool = connection_pool

    def find_all(self) -> List[User]:
        with self.connection_pool.get_resource() as connection:
            cursor = connection.cursor()
            selection = cursor.execute('SELECT * FROM users').fetchall()
            cursor.close()
            return list(map(self.__from_record, selection))

    @staticmethod
    def __from_record(record):
        return User(record[0], record[1], record[2])
