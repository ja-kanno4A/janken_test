import unittest
from unittest.mock import patch
from source.computer import computer_pon

class TestComp(unittest.TestCase):

    @patch('random.choice',side_effect=['グー'])
    def test_1(self,mock_choice):
        self.assertEqual(computer_pon(), "グー")

    @patch('random.choice',side_effect=['チョキ'])
    def test_2(self,mock_choice):
        self.assertEqual(computer_pon(), "チョキ")

    @patch('random.choice',side_effect=['パー'])
    def test_3(self,mock_choice):
        self.assertEqual(computer_pon(), "パー")

    
if __name__ == "__main__":
    TestComp()