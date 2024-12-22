import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Научный калькулятор")
        self.window.geometry("400x600")
        self.window.resizable(False, False)

        # Переменные
        self.current = ""
        self.memory = 0
        self.is_radian = tk.BooleanVar(value=True)
        
        # Дисплей
        self.display = tk.Entry(self.window, width=25, font=('Arial', 20), justify='right', state='readonly')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Кнопки режима градусы/радианы
        self.rad_deg_frame = ttk.LabelFrame(self.window, text="Режим")
        self.rad_deg_frame.grid(row=1, column=0, columnspan=4, pady=5)
        
        tk.Radiobutton(self.rad_deg_frame, text="Радианы", variable=self.is_radian, 
                      value=True).pack(side='left', padx=10)
        tk.Radiobutton(self.rad_deg_frame, text="Градусы", variable=self.is_radian, 
                      value=False).pack(side='left', padx=10)

        # Создание кнопок
        buttons = [
            'MC', 'MR', 'M+', 'M-',
            'sin', 'cos', 'tan', '√',
            'π', 'e', '±', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', 'C', '='
        ]

        row = 2
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.window, text=button, width=8, height=2, 
                     command=cmd).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, key):
        # В начале метода разблокируем дисплей
        self.display.config(state='normal')
        
        if key == '=':
            try:
                expression = self.current.replace('π', str(math.pi)).replace('e', str(math.e))
                if '/0' in expression:
                    raise ZeroDivisionError
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current = str(result)
            except (SyntaxError, NameError, ZeroDivisionError):
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Ошибка ввода")
                self.current = ""
        
        elif key == 'C':
            self.current = ""
            self.display.delete(0, tk.END)
        
        elif key == '±':
            if self.current and self.current[0] == '-':
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)
        
        elif key == 'π':
            self.current += str(math.pi)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)
        
        elif key == 'e':
            self.current += str(math.e)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)
        
        elif key in ['sin', 'cos', 'tan']:
            if not self.current:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Введите число")
                return
            try:
                num = float(self.current)
                if not self.is_radian.get():
                    num = math.radians(num)
                if key == 'sin':
                    result = math.sin(num)
                elif key == 'cos':
                    result = math.cos(num)
                else:
                    result = math.tan(num)
                self.current = str(round(result, 10))  # Округляем для читаемости
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.current)
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Неверный формат")
                self.current = ""
        
        elif key == '√':
            if not self.current:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Введите число")
                return
            try:
                num = float(self.current)
                if num < 0:
                    raise ValueError("Отрицательное число")
                result = math.sqrt(num)
                self.current = str(result)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.current)
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Недопустимое значение")
                self.current = ""
        
        # Операции с памятью
        elif key == 'MC':
            self.memory = 0
        elif key == 'MR':
            self.current = str(self.memory)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)
        elif key == 'M+':
            try:
                self.memory += float(self.current)
            except:
                pass
        elif key == 'M-':
            try:
                self.memory -= float(self.current)
            except:
                pass
        
        else:
            self.current += key
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current)

        # В конце метода снова блокируем дисплей
        self.display.config(state='readonly')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
