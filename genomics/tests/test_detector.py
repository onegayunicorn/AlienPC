import unittest
from genomics.src.synthetic_base_detection.detector import SyntheticBaseDetector

class TestSyntheticBaseDetector(unittest.TestCase):
    def test_detection_placeholder(self):
        detector = SyntheticBaseDetector()
        result = detector.detect("ATGCATGC")
        self.assertIn("synthetic_bases_found", result)
        self.assertIn("confidence", result)
        self.assertEqual(result["synthetic_bases_found"], 0)

if __name__ == "__main__":
    unittest.main()
