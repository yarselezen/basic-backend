class Command(object):

    def execute(self):
        pass


class CommandFactory(object):

    def create_user_command(self, first_name: str, last_name: str, phone: str) -> Command:
        pass
