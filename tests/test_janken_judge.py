import unittest
from unittest.mock import patch
from source.janken_judge import judge

class TestJudge(unittest.TestCase):
    def testpattern(self):
        patterns = [
           ('グー', 'グー','draw'),
           ('グー', 'チョキ','computer_win'),
           ('グー', 'パー','player_win'),
           
           ('チョキ', 'グー','player_win'),
           ('チョキ', 'チョキ','draw'),
           ('チョキ', 'パー','computer_win'),
           
           ('パー', 'グー','computer_win'),
           ('パー', 'チョキ','player_win'),
           ('パー', 'パー','draw'),
       ]
        
        for c, p, j in patterns:
           with self.subTest():
                self.assertEqual(judge(c,p),j)

if __name__ == "__main__":
    TestJudge()