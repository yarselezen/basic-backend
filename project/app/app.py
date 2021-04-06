from pathlib import Path

from bottle import Bottle, run

from project.adapter.command import DbCommandFactory
from project.app.handler import SayHello, GetUsers, CreateUser
from project.adapter.query import DbUserQueries
from project.lib.db_pool import DbConnectionPool


class App(object):

    def __init__(self, server: Bottle, host: str, port: int, db_path: Path):
        self.server = server
        self.host = host
        self.port = port
        self.db_path = db_path

    def launch(self):
        self.server.get('/')(
            SayHello().handle
        )
        self.server.get('/users')(
            GetUsers(
                DbUserQueries(DbConnectionPool(database=str(self.db_path.absolute()), capacity=5))
            ).handle
        )

        self.server.post('/users')(
            CreateUser(
                DbCommandFactory(DbConnectionPool(database=str(self.db_path.absolute()), capacity=5))
            ).handle
        )
        run(app=self.server, host=self.host, port=self.port)
