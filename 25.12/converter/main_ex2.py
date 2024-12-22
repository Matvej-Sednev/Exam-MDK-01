import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import json

class Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("Универсальный конвертер")
        
        # Создаем переменные для радиокнопок
        self.conversion_type = tk.StringVar(value="distance")
        
        # Создаем фреймы
        self.type_frame = ttk.LabelFrame(root, text="Тип конвертации")
        self.type_frame.pack(padx=10, pady=5, fill="x")
        
        # Радиокнопки для выбора типа конвертации
        ttk.Radiobutton(self.type_frame, text="Расстояние", value="distance", 
                       variable=self.conversion_type, command=self.update_units).pack(side="left", padx=5)
        ttk.Radiobutton(self.type_frame, text="Объём", value="volume", 
                       variable=self.conversion_type, command=self.update_units).pack(side="left", padx=5)
        ttk.Radiobutton(self.type_frame, text="Вес", value="weight", 
                       variable=self.conversion_type, command=self.update_units).pack(side="left", padx=5)
        ttk.Radiobutton(self.type_frame, text="Валюта", value="currency", 
                       variable=self.conversion_type, command=self.update_units).pack(side="left", padx=5)

        # Создаем основной фрейм для конвертации
        self.conv_frame = ttk.Frame(root)
        self.conv_frame.pack(padx=10, pady=5, fill="x")

        # Поля ввода и выпадающие списки
        self.amount_entry = ttk.Entry(self.conv_frame, width=15)
        self.amount_entry.grid(row=0, column=0, padx=5)
        
        self.from_unit = ttk.Combobox(self.conv_frame, width=15)
        self.from_unit.grid(row=0, column=1, padx=5)
        
        ttk.Label(self.conv_frame, text="→").grid(row=0, column=2, padx=5)
        
        self.to_unit = ttk.Combobox(self.conv_frame, width=15)
        self.to_unit.grid(row=0, column=3, padx=5)
        
        self.result_label = ttk.Label(self.conv_frame, text="")
        self.result_label.grid(row=1, column=0, columnspan=4, pady=10)

        # Кнопка конвертации
        ttk.Button(self.conv_frame, text="Конвертировать", 
                  command=self.convert).grid(row=2, column=0, columnspan=4, pady=5)

        # Словари для конвертации
        self.distance_units = {
            "Километры": 1000,
            "Метры": 1,
            "Сантиметры": 0.01,
            "Миллиметры": 0.001,
            "Мили": 1609.34,
            "Ярды": 0.9144,
            "Футы": 0.3048
        }

        self.volume_units = {
            "Кубические метры": 1000,
            "Литры": 1,
            "Миллилитры": 0.001,
            "Галлоны": 3.78541
        }

        self.weight_units = {
            "Килограммы": 1,
            "Граммы": 0.001,
            "Фунты": 0.453592,
            "Унции": 0.0283495
        }

        self.currency_rates = {}
        self.currency_names = {}
        self.update_currency_rates()
        self.update_units()

    def update_currency_rates(self):
        try:
            response = requests.get("http://www.cbr.ru/currency_base/daily/", timeout=5)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', class_='data')
            
            if not table:
                raise ValueError("Не удалось найти таблицу курсов валют")
            
            self.currency_rates = {"RUB": 1.0}
            self.currency_names = {"RUB": "Российский рубль"}
            
            for row in table.find_all('tr')[1:]:
                cols = row.find_all('td')
                if len(cols) >= 5:
                    currency_code = cols[1].text.strip()
                    currency_name = cols[3].text.strip()
                    rate = float(cols[4].text.strip().replace(',', '.'))
                    nominal = float(cols[2].text.strip())
                    self.currency_rates[currency_code] = rate / nominal
                    self.currency_names[currency_code] = f"{currency_code} - {currency_name}"
                
        except requests.RequestException:
            self.result_label.config(text="Ошибка получения курсов валют")
            # Резервные данные
            self.currency_rates = {"RUB": 1.0, "USD": 75.0, "EUR": 85.0}
            self.currency_names = {
                "RUB": "Российский рубль",
                "USD": "USD - Доллар США",
                "EUR": "EUR - Евро"
            }
        except Exception as e:
            self.result_label.config(text="Ошибка обработки курсов валют")
            self.currency_rates = {"RUB": 1.0, "USD": 75.0, "EUR": 85.0}
            self.currency_names = {
                "RUB": "Российский рубль",
                "USD": "USD - Доллар США",
                "EUR": "EUR - Евро"
            }

    def update_units(self):
        conversion_type = self.conversion_type.get()
        
        if conversion_type == "distance":
            units = list(self.distance_units.keys())
        elif conversion_type == "volume":
            units = list(self.volume_units.keys())
        elif conversion_type == "weight":
            units = list(self.weight_units.keys())
        else:  # currency
            units = list(self.currency_names.values())
            
        self.from_unit['values'] = units
        self.to_unit['values'] = units
        self.from_unit.set(units[0])
        self.to_unit.set(units[1])

    def convert(self):
        try:
            if not self.amount_entry.get().strip():
                self.result_label.config(text="Введите число для конвертации")
                return
            
            try:
                amount = float(self.amount_entry.get().replace(',', '.'))
            except ValueError:
                self.result_label.config(text="Пожалуйста, введите число")
                return
            
            if amount < 0:
                self.result_label.config(text="Пожалуйста, введите положительное число")
                return
            
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()
            
            if from_unit == to_unit:
                self.result_label.config(text=f"Результат: {amount:.4f}")
                return
            
            conversion_type = self.conversion_type.get()
            
            if conversion_type == "distance":
                result = amount * self.distance_units[from_unit] / self.distance_units[to_unit]
            elif conversion_type == "volume":
                result = amount * self.volume_units[from_unit] / self.volume_units[to_unit]
            elif conversion_type == "weight":
                result = amount * self.weight_units[from_unit] / self.weight_units[to_unit]
            else:  # currency
                # Ищем код валюты в полном названии
                from_code = next(code for code, name in self.currency_names.items() if name == from_unit)
                to_code = next(code for code, name in self.currency_names.items() if name == to_unit)
                
                if len(self.currency_rates) <= 3:
                    self.update_currency_rates()
                result = amount * self.currency_rates[from_code] / self.currency_rates[to_code]
                
            self.result_label.config(text=f"Результат: {result:.4f}")
        except StopIteration:
            self.result_label.config(text="Ошибка: неверная валюта")
        except Exception as e:
            self.result_label.config(text="Ошибка при конвертации")

if __name__ == "__main__":
    root = tk.Tk()
    app = Converter(root)
    root.mainloop()
