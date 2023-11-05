import redis
import json
import tkinter as tk
from tkinter import ttk


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
        self.settings_size_entry = NumericEntry(self.settings_frame)
        self.settings_color_combobox = ttk.Combobox(self.settings_frame)
        self.settings_font_style_combobox = ttk.Combobox(self.settings_frame)
        
        self.save_button = tk.Button(self, text='Сохранить')
        self.text_entry = tk.Entry(self)
        self.format_text = tk.Text(self)

        self.Pack()
        self.Config()
        self.LoadUsers()
        self.FillFont()
    
    def Pack(self):
        self.user_combobox.pack(side="top", pady=[10,20])
        
        self.settings_frame.pack(side="top", ipadx=10)
        self.settings_font_combobox.pack(side="top", pady=[10,10])
        self.settings_size_entry.pack(side="top", pady=[0,10])
        self.settings_color_combobox.pack(side="top", pady=[0,10])
        self.settings_font_style_combobox.pack(side="top", pady=[0,10])
        
        self.save_button.pack(side="top", pady=[10,20])
        self.text_entry.pack(side="top", pady=[0,10])
        self.format_text.pack(side="top", pady=[0,10])
    
    def Config(self):
        self.save_button.config(command=self.Save)
        
        self.user_combobox.config(state="readonly", width=40)
        self.user_combobox.bind("<<ComboboxSelected>>", self.LoadSettingsData)

        self.settings_font_combobox.config(state="readonly")
        self.settings_font_combobox.bind("<<ComboboxSelected>>", self.CopyEntryText)
        
        self.settings_color_combobox.config(state="readonly")
        self.settings_color_combobox.bind("<<ComboboxSelected>>", self.CopyEntryText)
        
        self.settings_font_style_combobox.config(state="readonly")
        self.settings_font_style_combobox.bind("<<ComboboxSelected>>", self.CopyEntryText)
        
        self.settings_size_entry.bind("<KeyRelease>", self.CopyEntryText)
        
        self.text_entry.config(width=40)
        self.text_entry.bind("<KeyRelease>", self.CopyEntryText)
        self.format_text.config(width=40, state='disabled')
        
    def Save(self):
        self.output_dict = {
                "full_name": f"{self.user_combobox.get()}",
                "settings": {
                    "font": f"{self.settings_font_combobox.get()}",
                    "size": int(self.settings_size_entry.get()),
                    "color": f"{self.settings_color_combobox.get()}",
                    "font_style": f"{self.settings_font_style_combobox.get()}"
                }
        }
        
        self.connection.set(self.GetUserKey().decode('utf-8'), json.dumps(self.output_dict))
        
        self.LoadUsers()
        self.LoadSettingsData(event=None)
        
    
    def FillFont(self):
        self.settings_font_combobox["values"] = ["Arial", "Verdana"]
        self.settings_color_combobox["values"] = ["red", "blue", "yellow", "green", "black"]
        self.settings_font_style_combobox["values"] = ["normal", "bold"]
    
    def LoadUsers(self):
        self.user_keys = self.connection.keys("user:*")
        self.user_data = [[key.decode('utf-8'), json.loads(self.connection.get(key))] for key in self.user_keys]
        self.user_names = [item[1].get("full_name") for item in self.user_data]
        self.user_combobox["values"] = self.user_names
        
    def LoadSettingsData(self, event):
        self.selected_name = self.user_combobox.get()
        self.settings_data_input = [item[1].get("settings") for item in self.user_data if item[1].get("full_name") == self.selected_name][0]
        
        self.settings_font_combobox.set(self.settings_data_input.get("font"))
        self.settings_size_entry.delete(0, "end")
        self.settings_size_entry.insert(0, self.settings_data_input.get("size"))
        self.settings_color_combobox.set(self.settings_data_input.get("color"))
        self.settings_font_style_combobox.set(self.settings_data_input.get("font_style"))
        
        self.CopyEntryText(event=None)
        
    def GetUserKey(self):
        for i,j in zip(self.user_keys, self.user_names):
            if j == self.user_combobox.get():
                user_key = i
                break
        return user_key
    
    def CopyEntryText(self, event):
        self.format_text.config(state="normal")
        self.format_text.delete(1.0, tk.END)
        
        self.format_text.tag_configure('style', font=(f"{self.settings_font_combobox.get()}", int(self.settings_size_entry.get()), f"{self.settings_font_style_combobox.get()}"), foreground=f"{self.settings_color_combobox.get()}",)
        
        self.format_text.insert(tk.END, self.text_entry.get(), 'style')
        self.format_text.config(state="disabled")


def fill_bd(connection: redis.StrictRedis):
    data = {
    "full_name": "Туманян Марк Михайлович",
    "settings": {
        "font": "Arial",
        "size": 10,
        "color": "red",
        "font_style": "normal"
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
        "font_style": "normal"
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
        "font_style": "bold"
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
    