import unittest
from src.calculator import calculate_tip, calculate_total, calculate_per_person


class TestCalculator(unittest.TestCase):
    def test_calculate_tip(self):
        self.assertAlmostEqual(calculate_tip(100, 10), 10.0)
        self.assertAlmostEqual(calculate_tip(50, 12), 6.0)
        self.assertAlmostEqual(calculate_tip(80, 0), 0.0)

    def test_calculate_total(self):
        self.assertAlmostEqual(calculate_total(100, 10), 110.0)
        self.assertAlmostEqual(calculate_total(50, 6), 56.0)

    def test_calculate_per_person(self):
        self.assertAlmostEqual(calculate_per_person(110, 2), 55.0)
        self.assertAlmostEqual(calculate_per_person(56, 1), 56.0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_tip(0, 10)
        with self.assertRaises(ValueError):
            calculate_tip(10, -1)
        with self.assertRaises(ValueError):
            calculate_total(10, -5)
        with self.assertRaises(ValueError):
            calculate_per_person(10, 0)


if __name__ == "__main__":
    unittest.main()