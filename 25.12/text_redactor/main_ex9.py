import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовый редактор")
        self.root.geometry("800x600")
        
        # Путь к файлу с историей
        self.history_file = "recent_files.txt"
        self.recent_files = self.load_recent_files()
        
        # Создание главного меню
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        
        # Меню "Файл"
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Новый", command=self.new_file)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        
        # Подменю недавних файлов
        self.recent_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="Недавние файлы", menu=self.recent_menu)
        self.update_recent_menu()
        
        # Меню "Правка"
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Правка", menu=self.edit_menu)
        self.edit_menu.add_command(label="Подсчет слов", command=self.count_words)
        self.edit_menu.add_command(label="Заменить текст", command=self.replace_text)
        
        # Текстовое поле
        self.text_area = tk.Text(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')
        
        self.current_file = None
        
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        
    def open_file(self, filename=None):
        if filename is None:
            filename = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, file.read())
                self.current_file = filename
                self.add_to_recent(filename)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл: {str(e)}")
                
    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.add_to_recent(self.current_file)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")
        else:
            self.save_as()
            
    def save_as(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            self.current_file = filename
            self.save_file()
            self.add_to_recent(filename)
            
    def count_words(self):
        text = self.text_area.get(1.0, tk.END).strip()
        words = len(text.split())
        messagebox.showinfo("Подсчет слов", f"Количество слов: {words}")
        
    def replace_text(self):
        # Создание диалогового окна для замены текста
        dialog = tk.Toplevel(self.root)
        dialog.title("Заменить текст")
        dialog.geometry("300x150")
        
        tk.Label(dialog, text="Найти:").pack(pady=5)
        find_entry = tk.Entry(dialog)
        find_entry.pack()
        
        tk.Label(dialog, text="Заменить на:").pack(pady=5)
        replace_entry = tk.Entry(dialog)
        replace_entry.pack()
        
        def do_replace():
            find_text = find_entry.get()
            replace_text = replace_entry.get()
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(find_text, replace_text)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, new_content)
            dialog.destroy()
            
        tk.Button(dialog, text="Заменить", command=do_replace).pack(pady=10)
        
    def load_recent_files(self):
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as file:
                    return [line.strip() for line in file.readlines()]
            return []
        except:
            return []
            
    def save_recent_files(self):
        try:
            with open(self.history_file, 'w', encoding='utf-8') as file:
                for filepath in self.recent_files:
                    file.write(filepath + '\n')
        except:
            pass
            
    def add_to_recent(self, filename):
        if filename in self.recent_files:
            self.recent_files.remove(filename)
        self.recent_files.insert(0, filename)
        self.recent_files = self.recent_files[:5]  # Хранить только 5 последних файлов
        self.save_recent_files()
        self.update_recent_menu()
        
    def update_recent_menu(self):
        self.recent_menu.delete(0, tk.END)
        for filename in self.recent_files:
            self.recent_menu.add_command(
                label=os.path.basename(filename),
                command=lambda f=filename: self.open_file(f)
            )

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
