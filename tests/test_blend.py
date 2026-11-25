import contextlib
import io
import math
from pathlib import Path
import runpy
import sys
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'api-mix'
sys.path.insert(0, str(SCRIPTS))


class LegacyRegressionTests(unittest.TestCase):
    def test_all_tank_volumes_are_included(self):
        for filename in ('api-mix-en.py', 'api-mix-th.py'):
            with patch('builtins.input', return_value='4'), contextlib.redirect_stdout(io.StringIO()):
                namespace = runpy.run_path(str(SCRIPTS / filename))
            for count, function in ((2, 'watermix_1'), (3, 'watermix_2'), (4, 'watermix_3')):
                with self.subTest(filename=filename, tanks=count):
                    values = iter(['100', '30'] * count + [''])
                    output = io.StringIO()
                    with patch('builtins.input', side_effect=lambda _: next(values)), contextlib.redirect_stdout(output):
                        namespace[function]()
                    self.assertIn('30.0', output.getvalue())

    def test_one_exit_after_calculation_exits_menu(self):
        for filename in ('api-mix-en.py', 'api-mix-th.py'):
            values = iter(['1', '100', '20', '100', '40', '', '4'])
            with self.subTest(filename=filename), patch('builtins.input', side_effect=lambda _: next(values)), contextlib.redirect_stdout(io.StringIO()):
                runpy.run_path(str(SCRIPTS / filename))


class BlendTests(unittest.TestCase):
    def test_weighted_result_and_total(self):
        from blend import calculate_blend
        self.assertEqual(calculate_blend([(100, 20), (300, 40)]), (400, 35))
        self.assertEqual(calculate_blend([(10, 30)] * 4), (40, 30))

    def test_zero_volume_tank_and_signed_api(self):
        from blend import calculate_blend
        self.assertEqual(calculate_blend([(0, 100), (10, -5)]), (10, -5))

    def test_invalid_inputs_are_rejected(self):
        from blend import calculate_blend
        for tanks in ([], [(1, 30)], [(1, 30)] * 5, [(0, 30)] * 2,
                      [(-1, 30), (1, 30)], [(math.nan, 30), (1, 30)],
                      [(1, math.inf), (1, 30)], [(1e308, 30)] * 2):
            with self.subTest(tanks=tanks), self.assertRaises(ValueError):
                calculate_blend(tanks)


if __name__ == '__main__':
    unittest.main()
