from pathlib import Path
import sys
import tkinter as tk
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'api-mix'))


class GuiTests(unittest.TestCase):
    def setUp(self):
        from oil_gui import App
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = App(self.root)

    def tearDown(self):
        self.root.update()
        self.root.destroy()

    def test_calculate_edit_and_clear(self):
        app = self.app
        app.volume_vars[0].set('100')
        app.api_vars[0].set('20')
        app.volume_vars[1].set('300')
        app.api_vars[1].set('40')
        app.calculate_button.invoke()
        self.assertIn('35.00', app.result.get())
        app.volume_vars[0].set('200')
        self.assertEqual(app.result.get(), '')
        app.clear_button.invoke()
        self.assertTrue(all(value.get() == '' for value in app.volume_vars + app.api_vars))

    def test_disabled_rows_are_ignored_and_count_clears_results(self):
        app = self.app
        for index in range(2):
            app.volume_vars[index].set('100')
            app.api_vars[index].set('30')
        app.volume_vars[2].set('bad')
        app.calculate()
        self.assertIn('30.00', app.result.get())
        app.tank_count.set('3')
        self.assertEqual(app.result.get(), '')
        app.calculate()
        self.assertNotEqual(app.error.get(), '')

    def test_invalid_fields_never_leave_old_results(self):
        for value in ('', 'bad', 'nan', 'inf', '-1'):
            app = self.app
            app.volume_vars[0].set('100')
            app.api_vars[0].set('30')
            app.volume_vars[1].set('100')
            app.api_vars[1].set('30')
            app.calculate()
            app.volume_vars[0].set(value)
            app.calculate()
            with self.subTest(value=value):
                self.assertEqual(app.result.get(), '')
                self.assertNotEqual(app.error.get(), '')


if __name__ == '__main__':
    unittest.main()
