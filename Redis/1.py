import redis
import json
import tkinter as tk
from tkinter import ttk, messagebox


class MainWindow(tk.Tk):
    def __init__(self, connection: redis.StrictRedis, parent = None):
        self.parent = parent
        super().__init__() 

        self.title("Потом чё-нибудь придумай")
        self.geometry("800x600")
        
        self.user_combobox = ttk.Combobox(self)
        
        self.settings_frame = tk.Frame(self, background="gray")
        self.settings_font_combobox = ttk.Combobox(self.settings_frame)
        self.settings_size_entry = tk.Entry(self.settings_frame)
        self.settings_color_combobox = ttk.Combobox(self.settings_frame)
        self.settings_font_style_combobox = ttk.Combobox(self.settings_frame)
        
        self.save_button = tk.Button(self)
        self.text_entry = tk.Entry(self)
        self.format_text_entry = tk.Entry(self)

        self.Pack()
        self.Config()
    
    def Pack(self):
        self.user_combobox.pack(side="top",pady=[10,20])
        
        self.settings_frame.pack(side="top", ipadx=10)
        self.settings_font_combobox.pack(side="top", pady=[10,10])
        self.settings_size_entry.pack(side="top", pady=[0,10])
        self.settings_color_combobox.pack(side="top", pady=[0,10])
        self.settings_font_style_combobox.pack(side="top", pady=[0,10])
        
        self.save_button.pack(side="top", pady=[10,20])
        self.text_entry.pack(side="top", pady=[0,10])
        self.format_text_entry.pack(side="top", pady=[0,10])
    
    def Config(self):
        self.save_button.config(command=self.Save)
        
    def Save(self):
        pass


def fill_bd(connection: redis.StrictRedis):
    data = {
    "full_name": "Туманян Марк Михайлович",
    "settings": {
        "font": "Arial",
        "size": 10,
        "color": "red",
        "font_style": "bold"
        }
    }
    data_json = json.dumps(data)
    key = "user:1"
    connection.set(key, data_json)
    
    data = {
    "full_name": "Рейно Кузьмин Степанович",
    "settings": {
        "font": "Verdana",
        "size": 15,
        "color": "yellow",
        "font_style": ""
        }
    }
    data_json = json.dumps(data)
    key = "user:2"
    connection.set(key, data_json)
    
    data = {
    "full_name": "Семёнов KarelianBear Андреевич",
    "settings": {
        "font": "Arial",
        "size": 6,
        "color": "blue",
        "font_style": "italic"
        }
    }
    data_json = json.dumps(data)
    key = "user:3"
    connection.set(key, data_json)
    
    # Десериализуйте данные из JSON в словарь
    stored_data = json.loads(connection.get("user:3"))

    # Выведите сохраненные данные
    print(stored_data)


if __name__ == "__main__":
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #fill_bd(r)
    
    main = MainWindow(connection=r)
    main.mainloop()
    