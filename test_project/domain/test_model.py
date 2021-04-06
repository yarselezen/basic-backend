from unittest import TestCase

from project.domain.model import User


class TestUser(TestCase):
    def test_as_dict(self):
        user = User('john', 'doe', '+79109700102')
        self.assertEqual(user.as_dict(), {'first_name': 'john', 'last_name': 'doe', 'phone': '+79109700102'})
