import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
import io
import json
from datetime import datetime
import sqlite3
from deep_translator import GoogleTranslator

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Погодное приложение")
        self.root.geometry("800x300")
        
        self.api_key = "dd3858fc9dd84660ac553814240912"
        self.translator = GoogleTranslator(source='auto', target='ru')
        
        # Словарь для перевода погодных условий
        self.weather_translations = {
            "Sunny": "Солнечно",
            "Clear": "Ясно",
            "Partly cloudy": "Переменная облачность",
            "Cloudy": "Облачно",
            "Overcast": "Пасмурно",
            "Mist": "Туман",
            "Patchy rain possible": "Возможен небольшой дождь",
            "Patchy snow possible": "Возможен небольшой снег",
            "Patchy sleet possible": "Возможен мокрый снег",
            "Patchy freezing drizzle possible": "Возможна изморось",
            "Thundery outbreaks possible": "Возможны грозы",
            "Blowing snow": "Метель",
            "Blizzard": "Буран",
            "Fog": "Туман",
            "Freezing fog": "Ледяной туман",
            "Patchy light drizzle": "Местами легкая морось",
            "Light drizzle": "Легкая морось",
            "Freezing drizzle": "Изморось",
            "Heavy freezing drizzle": "Сильная изморось",
            "Patchy light rain": "Местами небольшой дождь",
            "Light rain": "Небольшой дождь",
            "Moderate rain at times": "Временами умеренный дождь",
            "Moderate rain": "Умеренный дождь",
            "Heavy rain at times": "Временами сильный дождь",
            "Heavy rain": "Сильный дождь",
            "Light freezing rain": "Небольшой ледяной дождь",
            "Moderate or heavy freezing rain": "Умеренный или сильный ледяной дождь",
            "Light sleet": "Небольшой мокрый снег",
            "Moderate or heavy sleet": "Умеренный или сильный мокрый снег",
            "Patchy light snow": "Местами небольшой снег",
            "Light snow": "Небольшой снег",
            "Patchy moderate snow": "Местами умеренный снег",
            "Moderate snow": "Умеренный снег",
            "Patchy heavy snow": "Местами сильный снег",
            "Heavy snow": "Сильный снег",
            "Ice pellets": "Ледяной дождь",
            "Light rain shower": "Небольшой ливень",
            "Moderate or heavy rain shower": "Умеренный или сильный ливень",
            "Torrential rain shower": "Проливной дождь",
            "Light sleet showers": "Небольшой мокрый снег",
            "Moderate or heavy sleet showers": "Умеренный или сильный мокрый снег",
            "Light snow showers": "Небольшой снегопад",
            "Moderate or heavy snow showers": "Умеренный или сильный снегопад",
            "Light showers of ice pellets": "Небольшой ледяной дождь",
            "Moderate or heavy showers of ice pellets": "Умеренный или сильный ледяной дождь",
            "Patchy light rain with thunder": "Местами небольшой дождь с грозой",
            "Moderate or heavy rain with thunder": "Умеренный или сильный дождь с грозой",
            "Patchy light snow with thunder": "Местами небольшой снег с грозой",
            "Moderate or heavy snow with thunder": "Умеренный или сильный снег с грозой"
        }
        
        self.create_widgets()
        self.create_database()
        
    def create_widgets(self):
        # Фрейм для поиска по городу
        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=5, padx=10, fill='x')
        
        ttk.Label(search_frame, text="Поиск по городу:").pack(side='left', padx=5)
        self.location_entry = ttk.Entry(search_frame, width=40)
        self.location_entry.pack(side='left', padx=5)
        
        search_btn = ttk.Button(search_frame, text="Поиск", command=self.get_weather)
        search_btn.pack(side='left', padx=5)
        
        # Фрейм для поиска по координатам
        coords_frame = ttk.Frame(self.root)
        coords_frame.pack(pady=5, padx=10, fill='x')
        
        ttk.Label(coords_frame, text="Широта:").pack(side='left', padx=5)
        self.lat_entry = ttk.Entry(coords_frame, width=15)
        self.lat_entry.pack(side='left', padx=5)
        
        ttk.Label(coords_frame, text="Долгота:").pack(side='left', padx=5)
        self.lon_entry = ttk.Entry(coords_frame, width=15)
        self.lon_entry.pack(side='left', padx=5)
        
        coords_btn = ttk.Button(coords_frame, text="Поиск по координатам", 
                              command=self.get_weather_by_coords)
        coords_btn.pack(side='left', padx=5)
        
        history_btn = ttk.Button(coords_frame, text="История", command=self.show_history)
        history_btn.pack(side='left', padx=5)
        
        # Фрейм для отображения погоды
        self.weather_frame = ttk.Frame(self.root)
        self.weather_frame.pack(pady=10, padx=10, fill='both', expand=True)
        
        self.weather_label = ttk.Label(self.weather_frame, text="")
        self.weather_label.pack()
        
        self.image_label = ttk.Label(self.weather_frame)
        self.image_label.pack()

    def get_weather_by_coords(self):
        try:
            lat = self.lat_entry.get()
            lon = self.lon_entry.get()
            location = f"{lat},{lon}"
            self.get_weather_data(location)
        except Exception as e:
            self.weather_label.config(text=f"Ошибка: {str(e)}")

    def get_weather(self):
        location = self.location_entry.get()
        self.get_weather_data(location)

    def get_weather_data(self, location):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={location}"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            # Получение данных о погоде
            temp = data['current']['temp_c']
            condition_en = data['current']['condition']['text']
            wind_speed = data['current']['wind_kph']
            humidity = data['current']['humidity']
            icon_url = "https:" + data['current']['condition']['icon']
            location_name = data['location']['name']
            
            # Перевод названия места и условий
            try:
                location_translated = self.translator.translate(location_name)
            except:
                location_translated = location_name
                
            condition = self.weather_translations.get(condition_en, condition_en)
            
            # Загрузка иконки
            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)
            
            # Обновление интерфейса
            self.weather_label.config(
                text=f"Место: {location_translated}\n"
                     f"Температура: {temp}°C\n"
                     f"Условия: {condition}\n"
                     f"Скорость ветра: {wind_speed} км/ч\n"
                     f"Влажность: {humidity}%"
            )
            self.image_label.config(image=icon_photo)
            self.image_label.image = icon_photo
            
            # Сохранение в историю
            self.save_to_history(location_translated, temp, condition, wind_speed, humidity)
            
        except Exception as e:
            self.weather_label.config(text=f"Ошибка: {str(e)}")

    def create_database(self):
        conn = sqlite3.connect('weather_history.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT,
                temperature REAL,
                condition TEXT,
                wind_speed REAL,
                humidity INTEGER,
                timestamp DATETIME
            )
        ''')
        conn.commit()
        conn.close()
        
    def save_to_history(self, location, temp, condition, wind_speed, humidity):
        conn = sqlite3.connect('weather_history.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO history (location, temperature, condition, wind_speed, humidity, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (location, temp, condition, wind_speed, humidity, datetime.now()))
        conn.commit()
        conn.close()
        
    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("История запросов")
        history_window.geometry("800x400")
        
        tree = ttk.Treeview(history_window, columns=("Location", "Temperature", "Condition", "Wind", "Humidity", "Time"))
        tree.heading("Location", text="Место")
        tree.heading("Temperature", text="Температура")
        tree.heading("Condition", text="Условия")
        tree.heading("Wind", text="Ветер")
        tree.heading("Humidity", text="Влажность")
        tree.heading("Time", text="Время")
        
        # Настройка ширины колонок
        for column in tree["columns"]:
            tree.column(column, width=120)
        
        conn = sqlite3.connect('weather_history.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM history ORDER BY timestamp DESC')
        
        for row in cursor.fetchall():
            tree.insert("", 0, values=(
                row[1],                    # location
                f"{row[2]}°C",            # temperature
                row[3],                    # condition
                f"{row[4]} км/ч",         # wind_speed
                f"{row[5]}%",             # humidity
                row[6]                     # timestamp
            ))
            
        tree.pack(fill='both', expand=True)
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop() 