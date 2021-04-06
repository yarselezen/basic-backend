class User(object):
    def __init__(self, first_name: str, last_name: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def as_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone
        }
