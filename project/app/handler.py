import json

from bottle import BaseResponse, request

from project.domain.command import CommandFactory
from project.domain.query import UserQueries


class Handler:

    def handle(self) -> BaseResponse:
        pass


class SayHello(Handler):

    def handle(self) -> BaseResponse:
        return BaseResponse('Hello!')


class GetUsers(Handler):

    def __init__(self, user_queries: UserQueries):
        self.user_queries = user_queries

    def handle(self) -> BaseResponse:
        users = list(map(lambda user: user.as_dict(), self.user_queries.find_all()))
        return BaseResponse(
            body=json.dumps(users, sort_keys=True, indent=4),
            headers={'Content-Type': 'application/json'}
        )


class CreateUser(Handler):

    def __init__(self, command_factory: CommandFactory):
        self.command_factory = command_factory

    def handle(self) -> BaseResponse:
        body = request.json
        self.command_factory.create_user_command(
            body['first_name'],
            body['last_name'],
            body['phone']
        ).execute()
        return BaseResponse(status=201)
