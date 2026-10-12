import unittest

from src.toolkit.converter import convert
from src.toolkit.errors import ConvertError


class TestConverterResults(unittest.TestCase):
    def test_length(self):
        self.assertAlmostEqual(convert(5, "km", "cm"), 500000.0)
        self.assertAlmostEqual(convert(1, "m", "mm"), 1000.0)
        self.assertAlmostEqual(convert(250, "cm", "m"), 2.5)

    def test_mass(self):
        self.assertAlmostEqual(convert(1, "kg", "g"), 1000.0)
        self.assertAlmostEqual(convert(1, "tn", "kg"), 1000.0)
        self.assertAlmostEqual(convert(3, "cn", "kg"), 300.0)

    def test_temperature(self):
        self.assertAlmostEqual(convert(0, "c", "f"), 32.0)
        self.assertAlmostEqual(convert(100, "c", "k"), 373.15)

    def test_case_insensitive(self):
        self.assertAlmostEqual(convert(5, "KM", "Cm"), 500000.0)

    def test_string_value(self):
        self.assertAlmostEqual(convert("2.5", "m", "cm"), 250.0)

    def test_result_is_float(self):
        self.assertIsInstance(convert(1, "m", "m"), float)


class TestConverterErrors(unittest.TestCase):
    def test_unknown_unit(self):
        with self.assertRaises(ConvertError):
            convert(1, "mile", "m")
        with self.assertRaises(ConvertError):
            convert(1, "m", "foot")

    def test_incompatible_units(self):
        with self.assertRaises(ConvertError):
            convert(1, "km", "kg")
        with self.assertRaises(ConvertError):
            convert(1, "c", "m")

    def test_below_absolute_zero(self):
        with self.assertRaises(ConvertError):
            convert(-274, "c", "k")
        with self.assertRaises(ConvertError):
            convert(-1, "k", "c")
        with self.assertRaises(ConvertError):
            convert(-460, "f", "c")

if __name__ == "__main__":
    unittest.main()