import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout
from main import hand_cricket

class TestHandCricketSimple(unittest.TestCase):

    @patch('builtins.input', side_effect=["2", "3", "4"])  # user inputs
    @patch('random.randint', side_effect=[6, 6, 4])        # enemy guesses
    def test_simple_game_flow(self, _mock_randint, _mock_input):
        f = io.StringIO()
        with redirect_stdout(f):
            hand_cricket()
        output = f.getvalue()

        # Check basic expected outputs
        self.assertIn("enemy guess 6", output)
        self.assertIn("your current Score: 2", output)
        self.assertIn("your current Score: 5", output)
        self.assertIn("enemy guess 4", output)
        self.assertIn("------------you are out", output)

if __name__ == "__main__":
    unittest.main()
