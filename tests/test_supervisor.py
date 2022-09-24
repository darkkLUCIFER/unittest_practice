import unittest
from models import Supervisor


class SupervisorTestCase(unittest.TestCase):
    """
    Check Supervisor class attributes and methods
    """

    def setUp(self) -> None:
        self.supervisor = Supervisor.login('mahdi', '321')
        self.sample = Supervisor.sample()

    def test_all_data(self):
        self.assertIsInstance(self.sample, Supervisor, 'sample does not return proper instance')
        self.assertTrue(hasattr(self.sample, 'username'), 'instance does not have username')
        self.assertTrue(hasattr(self.sample, 'password'), 'instance does not have password')
        self.assertTrue(hasattr(self.sample, 'phone_number'), 'instance does not have phone number')

    def test_supervisor_protected_method(self):
        self.assertIsNone(self.sample.protected(), 'not raised on protected method')
        self.assertListEqual(self.supervisor.protected(), [1, 2, 3], 'protected data dont match')
