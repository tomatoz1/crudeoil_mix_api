"""Windows form for the project's existing API-weighting calculation."""
import tkinter as tk
from tkinter import ttk

from blend import calculate_blend


class App:
    def __init__(self, root):
        self.root = root
        root.title('Crude Oil Mixer')
        root.minsize(680, 580)
        root.geometry('740x620')
        root.configure(background='#f3f6fa')
        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure('.', font=('Tahoma', 11), background='#f3f6fa')
        style.configure('Title.TLabel', font=('Tahoma', 23, 'bold'), foreground='#173052')
        style.configure('Muted.TLabel', foreground='#53647a')
        style.configure('Result.TLabel', font=('Tahoma', 19, 'bold'), foreground='#12664f')
        style.configure('Error.TLabel', foreground='#b42318')
        style.configure('Accent.TButton', padding=(20, 10), background='#204f88', foreground='white')
        style.configure('TEntry', padding=7)
        self.tank_count = tk.StringVar(value='2')
        self.volume_vars = [tk.StringVar() for _ in range(4)]
        self.api_vars = [tk.StringVar() for _ in range(4)]
        self.result = tk.StringVar()
        self.total = tk.StringVar()
        self.error = tk.StringVar()
        page = ttk.Frame(root, padding=28)
        page.pack(fill='both', expand=True)
        page.columnconfigure(1, weight=1)
        page.columnconfigure(2, weight=1)
        ttk.Label(page, text='Crude Oil Mixer', style='Title.TLabel').grid(row=0, column=0, columnspan=3, sticky='w')
        ttk.Label(page, text='ผสมน้ำมัน 2–4 ถัง • ค่าเฉลี่ย API ถ่วงตามปริมาตร', style='Muted.TLabel').grid(row=1, column=0, columnspan=3, sticky='w', pady=(6, 20))
        ttk.Label(page, text='จำนวนถัง / Tanks').grid(row=2, column=0, sticky='w')
        count = ttk.Combobox(page, textvariable=self.tank_count, values=('2', '3', '4'), state='readonly', width=8)
        count.grid(row=2, column=1, sticky='w', pady=(0, 20))
        for column, heading in enumerate(('ถัง / Tank', 'ปริมาตร / Volume (bbl)', 'API')):
            ttk.Label(page, text=heading, style='Muted.TLabel').grid(row=3, column=column, sticky='w', pady=(0, 8))
        self.entries = []
        for index in range(4):
            ttk.Label(page, text=f'Tank {index + 1}').grid(row=index + 4, column=0, sticky='w', pady=6)
            row = []
            for column, variable in enumerate((self.volume_vars[index], self.api_vars[index]), 1):
                entry = ttk.Entry(page, textvariable=variable, width=16)
                entry.grid(row=index + 4, column=column, sticky='ew', padx=(0, 12), pady=6)
                variable.trace_add('write', self.invalidate)
                row.append(entry)
            self.entries.append(row)
        buttons = ttk.Frame(page)
        buttons.grid(row=8, column=0, columnspan=3, sticky='w', pady=(20, 14))
        self.calculate_button = ttk.Button(buttons, text='คำนวณ / Calculate', command=self.calculate, style='Accent.TButton')
        self.calculate_button.pack(side='left')
        self.clear_button = ttk.Button(buttons, text='ล้างค่า / Clear', command=self.clear, padding=(16, 10))
        self.clear_button.pack(side='left', padx=10)
        ttk.Label(page, textvariable=self.error, style='Error.TLabel', wraplength=620).grid(row=9, column=0, columnspan=3, sticky='w')
        ttk.Label(page, textvariable=self.result, style='Result.TLabel').grid(row=10, column=0, columnspan=3, sticky='w', pady=(14, 4))
        ttk.Label(page, textvariable=self.total, style='Muted.TLabel').grid(row=11, column=0, columnspan=3, sticky='w')
        ttk.Label(page, text='ใช้สูตรถ่วงค่า API เดิมของโปรเจกต์ • ไม่ได้แปลงเป็น Specific Gravity', style='Muted.TLabel', wraplength=620).grid(row=12, column=0, columnspan=3, sticky='sw', pady=(20, 0))
        page.rowconfigure(12, weight=1)
        self.tank_count.trace_add('write', self.update_rows)
        self.update_rows()
        self.entries[0][0].focus_set()
        root.bind('<Return>', lambda event: self.calculate())

    def invalidate(self, *_):
        self.result.set('')
        self.total.set('')
        self.error.set('')

    def update_rows(self, *_):
        for index, entries in enumerate(self.entries):
            for entry in entries:
                entry.configure(state='normal' if index < int(self.tank_count.get()) else 'disabled')
        self.invalidate()

    def calculate(self):
        self.invalidate()
        try:
            tanks = []
            for index in range(int(self.tank_count.get())):
                values = []
                for column, variable in enumerate((self.volume_vars[index], self.api_vars[index])):
                    try:
                        values.append(float(variable.get().strip()))
                    except ValueError:
                        self.entries[index][column].focus_set()
                        raise ValueError(f'Tank {index + 1}: กรุณากรอกตัวเลขให้ครบ / enter a number.') from None
                tanks.append(tuple(values))
            total, average = calculate_blend(tanks)
        except ValueError as error:
            self.error.set(str(error))
            return
        self.result.set(f'API เฉลี่ย / Weighted API   {average:,.2f}')
        self.total.set(f'ปริมาตรรวม / Total volume   {total:,.2f} bbl')

    def clear(self):
        for variable in self.volume_vars + self.api_vars:
            variable.set('')
        self.invalidate()
        self.entries[0][0].focus_set()


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
