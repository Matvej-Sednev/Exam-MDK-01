import tkinter as tk
from tkinter import colorchooser, messagebox
from datetime import datetime

class DrawingNotebook:
    def __init__(self, root):
        try:
            self.root = root
            self.root.title("Графический блокнот")
            
            # Минимальный размер окна
            self.root.minsize(400, 300)
            
            # Создаем холст с обработкой ошибок
            try:
                self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
                self.canvas.pack(expand=True, fill='both')
            except Exception as e:
                messagebox.showerror("Ошибка", "Не удалось создать холст")
                return
            
            # Кнопка выбора цвета с обработкой ошибок
            try:
                self.color_button = tk.Button(root, text="Выбрать цвет", command=self.choose_color)
                self.color_button.pack()
            except Exception as e:
                messagebox.showerror("Ошибка", "Не удалось создать кнопку выбора цвета")
                return
            
            # Текущий цвет
            self.current_color = 'black'
            
            # Координаты для рисования
            self.prev_x = None
            self.prev_y = None
            
            # Лог действий
            self.drawing_log = []
            
            # Максимальный размер лога
            self.max_log_size = 1000
            
            # Привязываем события мыши с обработкой ошибок
            try:
                self.canvas.bind('<Button-1>', self.start_drawing)
                self.canvas.bind('<B1-Motion>', self.draw)
                self.canvas.bind('<ButtonRelease-1>', self.stop_drawing)
            except Exception as e:
                messagebox.showerror("Ошибка", "Не удалось привязать события мыши")
                return
            
            # Добавляем кнопку очистки холста
            self.clear_button = tk.Button(root, text="Очистить холст", command=self.clear_canvas)
            self.clear_button.pack()
        except Exception as e:
            messagebox.showerror("Ошибка инициализации", "Не удалось инициализировать приложение")
            raise

    def choose_color(self):
        try:
            color = colorchooser.askcolor(title="Выберите цвет")[1]
            if color:  # Проверяем, был ли выбран цвет
                self.current_color = color
        except Exception as e:
            messagebox.showerror("Ошибка", "Не удалось выбрать цвет")
            self.current_color = 'black'  # Возвращаемся к черному цвету по умолчанию

    def start_drawing(self, event):
        try:
            self.prev_x = event.x
            self.prev_y = event.y
        except Exception as e:
            self.prev_x = None
            self.prev_y = None

    def draw(self, event):
        try:
            if self.prev_x and self.prev_y:
                x, y = event.x, event.y
                # Проверяем, находятся ли координаты в пределах холста
                if 0 <= x <= self.canvas.winfo_width() and 0 <= y <= self.canvas.winfo_height():
                    self.canvas.create_line(self.prev_x, self.prev_y, x, y, 
                                         fill=self.current_color, width=2)
                    
                    # Ограничиваем размер лога
                    if len(self.drawing_log) < self.max_log_size:
                        self.drawing_log.append(f"Line: from ({self.prev_x},{self.prev_y}) "
                                             f"to ({x},{y}) color: {self.current_color}")
                    
                    self.prev_x = x
                    self.prev_y = y
        except Exception as e:
            messagebox.showerror("Ошибка", "Ошибка при рисовании")
            self.prev_x = None
            self.prev_y = None

    def stop_drawing(self, event):
        try:
            self.save_to_file()
            self.prev_x = None
            self.prev_y = None
        except Exception as e:
            messagebox.showerror("Ошибка", "Не удалось сохранить рисунок")

    def save_to_file(self):
        if not self.drawing_log:  # Если лог пустой, не создаем файл
            return
            
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"drawing_log_{timestamp}.txt"
            with open(filename, 'a', encoding='utf-8') as f:
                for line in self.drawing_log:
                    f.write(line + '\n')
            self.drawing_log = []
        except Exception as e:
            messagebox.showerror("Ошибка", "Не удалось сохранить файл")
            self.drawing_log = []  # Очищаем лог в случае ошибки

    def clear_canvas(self):
        try:
            self.canvas.delete("all")  # Очищаем весь холст
            self.drawing_log = []  # Очищаем лог
        except Exception as e:
            messagebox.showerror("Ошибка", "Не удалось очистить холст")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = DrawingNotebook(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Критическая ошибка", "Не удалось запустить приложение")
