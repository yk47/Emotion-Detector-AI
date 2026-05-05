import unittest
from emotion_detector import analyze_emotion

class TestEmotion(unittest.TestCase):

    def test_valid_input(self):
        result = analyze_emotion("I am very happy")
        self.assertIsNotNone(result)

    def test_empty_input(self):
        result = analyze_emotion("")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
