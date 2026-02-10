import unittest
from genomics.src.synthetic_base_detection.detector import detect

class TestSyntheticBaseDetector(unittest.TestCase):
    def test_detection_placeholder(self):
        result = detect("ATGCATGC")
        self.assertIn("synthetic_bases", result)
        self.assertIn("confidence", result)
        self.assertEqual(result["synthetic_bases"], 0)

    def test_detect_simple(self):
        self.assertEqual(detect("XXXYZZ")["synthetic_bases"], 1)

if __name__ == "__main__":
    unittest.main()
