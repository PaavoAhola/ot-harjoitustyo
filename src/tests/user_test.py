import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def test_username_cannot_be_changed(self):
        user = User("PelleHermanni69", "123456789")
        user.name = "molli"
        name = user.return_name()

        self.assertEqual(name, "PelleHermanni69")
