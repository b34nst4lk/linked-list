import unittest
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = SinglyLinkedList(1, 2, 3)

    def test_that_list_inits_correctly(self):
        self.assertEqual(self.list[0], 1)
        self.assertEqual(self.list[1], 2)
        self.assertEqual(self.list[2], 3)

if __name__ == "__main__":
    unittest.main()