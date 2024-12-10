import unittest
from unittest.mock import patch
from source.player import player_pon

class TestPlayer(unittest.TestCase):

    @patch('builtins.input',side_effect=['1'])
    # side_effectは複数できるやつ（引数）
    def test_rock(self,mock_input):
        # result = player_pon(1)
        self.assertEqual(player_pon(), "グー")
        # mock_input.assert_called_once_with("グー、チョキ、パーのいずれかを入力してください：")
   
    @patch('builtins.input',side_effect=['2'])
    def test_scissors(self,mock_input):
        result = player_pon()
        self.assertEqual(result, "チョキ")


    @patch('builtins.input',side_effect=['3'])
    def test_paper(self,mock_input):
        result =player_pon()
        self.assertEqual(result, "パー")

    
    @patch('builtins.input')
    def test_input_cccddd(self, mock_input):
       mock_input.side_effect = ['0', '4']
       self.assertNotEqual(player_pon, 'グー'or'チョキ'or'パー')
    
if __name__ == "__main__":
    TestPlayer()
