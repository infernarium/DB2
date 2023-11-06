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
        self.geometry("300x450")
        
        self.referee_combobox = ttk.Combobox(self)
        self.setted_point_entry = NumericEntry(self)
        self.sportsman_combobox = ttk.Combobox(self)
        self.save_button = tk.Button(self, text='Сохранить')
        self.rating_list = tk.Listbox(self)

        self.Pack()
        self.Config()
        self.LoadReferee()
        self.FillRating()
    
    def Pack(self):
        self.referee_combobox.pack(side="top", pady=[10,0])
        self.setted_point_entry.pack(side="top", pady=[10,10])
        self.sportsman_combobox.pack(side="top", pady=[0,10])
        self.save_button.pack(side="top", pady=[0,20])
        self.rating_list.pack(side="top", pady=[10,10])
    
    def Config(self):
        self.save_button.config(command=self.Save)
        
        self.referee_combobox.config(state="readonly", width=40)
        self.sportsman_combobox.config(state="readonly", width=40)
        
        self.rating_list.config(width=60)
        
    def Save(self):
        print("Сохранил, красавец!")
        RefereeSportsmenPoints = self.GetRefereeSportsmenPoints(self.referee_combobox.get())
        return
        self.output_dict = {
        "full_name": f"{self.referee_combobox.get()}",
        "points": [
            {"full_name": "Лева Дмитрий Сергеевич", "point" : int(RefereeSportsmenPoints[0] if (self.sportsman_combobox.get() != "Лева Дмитрий Сергеевич") else RefereeSportsmenPoints[0] + self.setted_point_entry.get())},
            {"full_name": "Семёнов KarelianBear Андреевич", "point" : int(RefereeSportsmenPoints[1] if (self.sportsman_combobox.get() != "Лева Дмитрий Сергеевич") else RefereeSportsmenPoints[1] + self.setted_point_entry.get())},
            {"full_name": "Рейно Кузьмин Степанович", "point" : int(RefereeSportsmenPoints[2] if (self.sportsman_combobox.get() != "Лева Дмитрий Сергеевич") else RefereeSportsmenPoints[2] + self.setted_point_entry.get())},
            ]
        }
        
        self.connection.set(self.GetRefereeKey().decode('utf-8'), json.dumps(self.output_dict))
    
    def LoadReferee(self):
        self.referee_keys = self.connection.keys("referee:*")
        self.referee_data = [json.loads(self.connection.get(key)) for key in self.referee_keys]
        self.referee_names = [item["full_name"] for item in self.referee_data]
        self.sportsman_names = [item["full_name"] for item in self.referee_data[0]["points"]] #['Лева Дмитрий Сергеевич', 'Семёнов KarelianBear Андреевич', 'Рейно Кузьмин Степанович']
        
        self.referee_combobox["values"] = self.referee_names
        self.sportsman_combobox["values"] = self.sportsman_names
        
    def GetRefereeKey(self):
        for i,j in zip(self.referee_keys, self.referee_names):
            if j == self.referee_combobox.get():
                user_key = i
                break
        return user_key.decode('utf-8')
    
    def FillRating(self):
        self.rating_list.delete(0, tk.END)
        sportsmen_list = [[name, self.GetPointsSum(name)] for name in self.sportsman_names]

        for sportsman in sorted(sportsmen_list, key=lambda x: x[1], reverse=True):
            self.rating_list.insert(tk.END, f"{sportsman[0]} - {sportsman[1]}")
            
    def GetPointsSum(self, sportsman_name):
        total_points = 0
        
        for referee in self.referee_data:
            for point_data in referee["points"]:
                if point_data["full_name"] == sportsman_name:
                    total_points += point_data["point"]
                    
        return total_points
    
    def GetRefereeSportsmenPoints(self, referee_name):
        for referee in self.referee_data:
            if referee["full_name"] == referee_name:
                return [point["point"] for point in [chel for chel in referee["points"]]]
        
    


def fill_bd(connection: redis.StrictRedis):
    data = {
    "full_name": "Судья Дредд",
    "points": [
        {"full_name": "Лева Дмитрий Сергеевич", "point" : 5},
        {"full_name": "Семёнов KarelianBear Андреевич", "point" : 10},
        {"full_name": "Рейно Кузьмин Степанович", "point" : 15},
        ]
    }
    connection.set("referee:1", json.dumps(data))
    data = {
    "full_name": "Родион Романович Раскольников",
    "points": [
        {"full_name": "Лева Дмитрий Сергеевич", "point" : 12},
        {"full_name": "Семёнов KarelianBear Андреевич", "point" : 4},
        {"full_name": "Рейно Кузьмин Степанович", "point" : 7},
        ]
    }
    connection.set("referee:2", json.dumps(data))
    data = {
    "full_name": "Александр Андреевич Чацкий",
    "points": [
        {"full_name": "Лева Дмитрий Сергеевич", "point" : 10},
        {"full_name": "Семёнов KarelianBear Андреевич", "point" : 11},
        {"full_name": "Рейно Кузьмин Степанович", "point" : 1},
        ]
    }
    connection.set("referee:3", json.dumps(data))


if __name__ == "__main__":
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #fill_bd(r)
    main = MainWindow(connection=r)
    main.mainloop()
    