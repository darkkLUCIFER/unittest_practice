import unittest
from models import Supervisor


class SupervisorTestCase(unittest.TestCase):
    """
    Check Supervisor class attributes and methods
    """

    def setUp(self) -> None:
        pass

    def test_all_data(self):
        instance = Supervisor.sample()
        self.assertIsInstance(instance, Supervisor, 'sample does not return proper instance')
        self.assertTrue(hasattr(instance, 'username'), 'instance does not have username')
        self.assertTrue(hasattr(instance, 'password'), 'instance does not have password')
        self.assertTrue(hasattr(instance, 'phone_number'), 'instance does not have phone number')
