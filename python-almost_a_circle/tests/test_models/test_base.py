import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_constructor_with_id(self):
        b = Base(1)
        self.assertEqual(b.id, 1)

    def test_constructor_without_id(self):
        b = Base()
        self.assertIsNotNone(b.id)

