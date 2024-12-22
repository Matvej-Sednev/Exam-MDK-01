import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from math import *

class GraphPlotter:
    def __init__(self, root):
        self.root = root
        self.root.title("Построитель графиков")
        
        # Создаем переменные
        self.selected_function = tk.StringVar(value="sin")
        self.custom_function = tk.StringVar()
        self.x_min = tk.DoubleVar(value=-10)
        self.x_max = tk.DoubleVar(value=10)
        self.points = tk.IntVar(value=1000)
        
        # Создаем интерфейс
        self.create_widgets()
        
    def create_widgets(self):
        # Фрейм для выбора функции
        function_frame = ttk.LabelFrame(self.root, text="Выбор функции")
        function_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        ttk.Radiobutton(function_frame, text="Sin(x)", variable=self.selected_function, 
                       value="sin", command=self.update_plot).pack(anchor="w")
        ttk.Radiobutton(function_frame, text="1/x", variable=self.selected_function,
                       value="inverse", command=self.update_plot).pack(anchor="w")
        ttk.Radiobutton(function_frame, text="x²", variable=self.selected_function,
                       value="square", command=self.update_plot).pack(anchor="w")
        ttk.Radiobutton(function_frame, text="√x", variable=self.selected_function,
                       value="sqrt", command=self.update_plot).pack(anchor="w")
        ttk.Radiobutton(function_frame, text="Своя функция", variable=self.selected_function,
                       value="custom", command=self.update_plot).pack(anchor="w")
        
        # Фрейм для пользовательской функции
        custom_frame = ttk.LabelFrame(self.root, text="Пользовательская функция")
        custom_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        ttk.Entry(custom_frame, textvariable=self.custom_function).pack(fill="x", padx=5, pady=5)
        ttk.Label(custom_frame, text="Примеры: sin(x) + x**2, exp(x), log(abs(x)), x**3 + 2*x").pack()
        
        # Фрейм для настроек
        settings_frame = ttk.LabelFrame(self.root, text="Настройки")
        settings_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        
        ttk.Label(settings_frame, text="X min:").grid(row=0, column=0)
        ttk.Entry(settings_frame, textvariable=self.x_min, width=10).grid(row=0, column=1)
        
        ttk.Label(settings_frame, text="X max:").grid(row=1, column=0)
        ttk.Entry(settings_frame, textvariable=self.x_max, width=10).grid(row=1, column=1)
        
        ttk.Label(settings_frame, text="Точки:").grid(row=2, column=0)
        ttk.Entry(settings_frame, textvariable=self.points, width=10).grid(row=2, column=1)
        
        ttk.Button(settings_frame, text="Обновить", command=self.update_plot).grid(row=3, column=0, columnspan=2)
        
        # Создаем область для графика
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().grid(row=0, column=1, rowspan=3, padx=5, pady=5)
        
        # Создаем таблицу значений
        self.table_text = tk.Text(self.root, height=10, width=30, state='disabled')
        self.table_text.grid(row=3, column=1, padx=5, pady=5)
        
        self.update_plot()
        
    def calculate_function(self, x):
        func_type = self.selected_function.get()
        
        if func_type == "sin":
            return np.sin(x)
        elif func_type == "inverse":
            mask = x != 0
            result = np.full_like(x, np.nan, dtype=float)
            result[mask] = 1.0 / x[mask]
            return result
        elif func_type == "square":
            return x**2
        elif func_type == "sqrt":
            mask = x >= 0
            result = np.full_like(x, np.nan, dtype=float)
            result[mask] = np.sqrt(x[mask])
            return result
        elif func_type == "custom":
            try:
                # Создаем безопасное пространство имен для eval
                safe_dict = {
                    'sin': np.sin,
                    'cos': np.cos,
                    'tan': np.tan,
                    'sqrt': np.sqrt,
                    'exp': np.exp,
                    'log': np.log,
                    'pi': np.pi,
                    'e': np.e,
                    'abs': np.abs,
                    'x': x,
                    'np': np
                }
                # Выполняем пользовательскую функцию
                return eval(self.custom_function.get(), {"__builtins__": {}}, safe_dict)
            except Exception as e:
                print(f"Ошибка в пользовательской функции: {e}")
                return np.zeros_like(x)
    
    def update_plot(self):
        self.ax.clear()
        
        # Ограничиваем количество точек
        max_points = 10000  # Максимальное количество точек
        points = min(self.points.get(), max_points)
        
        # Получаем значения x и y
        x = np.linspace(self.x_min.get(), self.x_max.get(), points)
        y = self.calculate_function(x)
        
        # Строим график
        self.ax.plot(x, y)
        self.ax.grid(True)
        self.ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        self.ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
        
        self.canvas.draw()
        
        # Обновляем таблицу значений
        self.update_table(x, y)
    
    def update_table(self, x, y):
        # Временно разрешаем редактирование для обновления
        self.table_text.config(state='normal')
        
        self.table_text.delete(1.0, tk.END)
        self.table_text.insert(tk.END, "x\t\ty\n")
        self.table_text.insert(tk.END, "-" * 30 + "\n")
        
        # Выводим только 10 значений для краткости
        step = max(len(x) // 10, 1)  # Убедимся, что шаг не меньше 1
        for i in range(0, len(x), step):
            # Пропускаем значения nan
            if not np.isnan(y[i]):
                self.table_text.insert(tk.END, f"{x[i]:.2f}\t\t{y[i]:.2f}\n")
        
        # Снова запрещаем редактирование
        self.table_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphPlotter(root)
    root.mainloop()
