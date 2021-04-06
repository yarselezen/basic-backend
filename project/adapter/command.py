from project.domain.command import Command, CommandFactory
from project.lib.db_pool import DbConnectionPool


class DbCreateUserCommand(Command):

    def __init__(self, connection_pool: DbConnectionPool, first_name: str, last_name: str, phone: str):
        self.connection_pool = connection_pool
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def execute(self):
        with self.connection_pool.get_resource() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (self.first_name, self.last_name, self.phone))
            connection.commit()
            cursor.close()


class DbCommandFactory(CommandFactory):
    def __init__(self, connection_pool: DbConnectionPool):
        self.connection_pool = connection_pool

    def create_user_command(self, first_name: str, last_name: str, phone: str):
        return DbCreateUserCommand(self.connection_pool, first_name, last_name, phone)
