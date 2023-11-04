import redis
import json
import tkinter as tk
from tkinter import ttk, messagebox


class NumericEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        # Регистрируем функцию валидации
        self.validate_input = master.register(self.validate)
        super().__init__(master, validate="key", validatecommand=(self.validate_input, '%P'), **kwargs)

    def validate(self, new_text):
        if (new_text == "" or new_text.isdigit()):
            return True
        return False

class MainWindow(tk.Tk):
    def __init__(self, connection: redis.StrictRedis, parent = None):
        self.parent = parent
        super().__init__() 
        
        self.connection = connection
        
        self.title("Потом чё-нибудь придумай")
        self.geometry("200x400")
        
        self.user_combobox = ttk.Combobox(self)
        
        self.settings_frame = tk.Frame(self, background="gray")
        self.settings_font_combobox = ttk.Combobox(self.settings_frame)
        
        self.dfhgadfhafdhg = (self.ValidateSize, "%P")
        
        self.settings_size_entry = NumericEntry(self.settings_frame)
        self.settings_color_combobox = ttk.Combobox(self.settings_frame)
        self.settings_font_style_combobox = ttk.Combobox(self.settings_frame)
        
        self.save_button = tk.Button(self)
        self.text_entry = tk.Entry(self)
        self.format_text_entry = tk.Entry(self)

        self.Pack()
        self.Config()
        self.LoadUsers()
        self.FillFont()
    
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
        
        self.user_combobox.config(state="readonly", width=40)
        self.user_combobox.bind("<<ComboboxSelected>>", self.LoadSettingsData)
        
        self.settings_size_entry.bind()
        
        self.settings_font_combobox.config(state="readonly")
        self.settings_color_combobox.config(state="readonly")
        self.settings_font_style_combobox.config(state="readonly")
        
    def Save(self):
        pass
    
    def FillFont(self):
        self.settings_font_combobox["values"] = ["Arial", "Verdana"]
        self.settings_color_combobox["values"] = ["Red", "Blue", "Yellow", "Green", "Black"]
        self.settings_font_style_combobox["values"] = ["Thin", "Regular", "Bold"]
    
    def LoadUsers(self):
        self.user_keys = self.connection.keys("user:*")
        self.user_data = [[key.decode('utf-8'), json.loads(self.connection.get(key))] for key in self.user_keys]
        self.user_names = [item[1].get("full_name") for item in self.user_data]
        self.user_combobox["values"] = self.user_names
        
    def LoadSettingsData(self, event):
        self.selected_name = self.user_combobox.get()
        self.settings_data = [item[1].get("settings") for item in self.user_data if item[1].get("full_name") == self.selected_name][0]
        
        self.settings_font_combobox.set(self.settings_data.get("font"))
        self.settings_size_entry.delete(0, "end")
        self.settings_size_entry.insert(0, self.settings_data.get("size"))
        self.settings_color_combobox.set(self.settings_data.get("color"))
        self.settings_font_style_combobox.set(self.settings_data.get("font_style"))
        
        


def fill_bd(connection: redis.StrictRedis):
    data = {
    "full_name": "Туманян Марк Михайлович",
    "settings": {
        "font": "Arial",
        "size": 10,
        "color": "red",
        "font_style": "Thin"
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
        "font_style": "Regular"
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
        "font_style": "Bold"
        }
    }
    data_json = json.dumps(data)
    key = "user:3"
    connection.set(key, data_json)


if __name__ == "__main__":
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #fill_bd(r)
    
    main = MainWindow(connection=r)
    main.mainloop()
    