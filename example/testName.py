import unittest
from Name import Name

class TestName(unittest.TestCase):
    def setUp(self):
        self.name = Name()
    def test_name(self):
        self.assertEqual(self.name.client("qwer"), "qwer")