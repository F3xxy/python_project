import contextlib
import io
import unittest

from toolkit.__main__ import main


def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = main(list(args))
        except SystemExit as exit_info:
            code = exit_info.code
    return code, out.getvalue(), err.getvalue()


class TestCli(unittest.TestCase):
    def test_calc_success(self):
        code, out, err = run("calc", "2 * (3 + 4) - 5")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "9.0")
        self.assertEqual(err, "")

    def test_calc_leading_minus(self):
        code, out, _ = run("calc", "-(2 + 3)")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "-5.0")

    def test_calc_error(self):
        code, out, err = run("calc", "1 / 0")
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertNotEqual(err.strip(), "")

    def test_convert_success(self):
        code, out, _ = run("convert", "5", "--from", "km", "--to", "cm")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "500000.0")

    def test_convert_negative_value(self):
        code, out, _ = run("convert", "-5", "--from", "C", "--to", "F")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "23.0")

    def test_convert_error(self):
        code, out, err = run("convert", "1", "--from", "km", "--to", "kg")
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertNotEqual(err.strip(), "")

    def test_no_command(self):
        code, _, _ = run()
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()