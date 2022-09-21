import unittest


class SampleTest(unittest.TestCase):
    """

    """

    def setUp(self) -> None:
        pass

    def test_sample_data_test(self):
        self.assertTrue()
        # assert a is True
        # assert bool(a)

        self.assertIn()
        # assert a in b

        self.assertIsInstance()
        # assert isinstance(a, list)

        self.assertIsNone()

        self.assertListEqual()

        self.assertRaises()

    def test_second_sample_data_test(self):
        self.assertTrue()

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
