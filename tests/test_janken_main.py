import unittest
from unittest.mock import patch
from source.janken_main import wh, res


class TestMain_loop(unittest.TestCase):
    @patch('source.player.player_pon',return_value="グー")
    @patch('source.computer.computer_pon',return_value="チョキ")
    @patch('source.janken_judge.judge',return_value="player_win")
    #test_~じゃないとテストコードと認識されない
    def test_pw(self,mock_p,mock_c,mock_j):
        round, player_win,computer_win,result = wh(1,0,0,"")
        self.assertEqual(round,2)
        self.assertEqual(player_win,1)
        self.assertEqual(computer_win,0)
        self.assertEqual(result,"player_win")

    @patch('source.player.player_pon',return_value="グー")
    @patch('source.computer.computer_pon',return_value="グー")
    @patch('source.janken_judge.judge',return_value="draw")
    def test_dr(self,mock_p,mock_c,mock_j):
        round, player_win, computer_win, result = wh(2,1,0,"")
        self.assertEqual(round,2)
        self.assertEqual(player_win,1)
        self.assertEqual(computer_win,0)
        self.assertEqual(result,"draw")

    @patch('source.player.player_pon',return_value="グー")
    @patch('source.computer.computer_pon',return_value="パー")
    @patch('source.janken_judge.judge',return_value="computer_win")
    def test_cw(self,mock_p,mock_c,mock_j):
        round, player_win,computer_win,result = wh(2,1,0,"")
        self.assertEqual(round,3)
        self.assertEqual(player_win,1)
        self.assertEqual(computer_win,1)
        self.assertEqual(result,"computer_win")

class TestMain_res(unittest.TestCase):
    def test_plwin(self):
        patterns = [
           (3, 0,'あなたの総合勝利です！'),
           (0, 3,'コンピュータの総合勝利です！'),
           (1, 2,'コンピュータの総合勝利です！'),
           (2, 1,'あなたの総合勝利です！'),
        ]
        for c, p, j in patterns:
           with self.subTest():
                self.assertEqual(res(c,p),j)
    
if __name__ == "__main__":
    # TestMain_loop()
    TestMain_res()