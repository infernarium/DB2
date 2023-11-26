from pymongo import MongoClient
import tkinter as tk

client = MongoClient('mongodb://192.168.112.103')
db = client['22303']
collection = db['tumanyan']

pattern_team = {
    'type': 'team',
    'name': '',
    'city': '',
    'coach name': '', 
    'players': [
        {
            'name': '', 
            'position': ''
        }
    ],
    'reserve players': [
        ''
    ]
}

pattern_game = {
    'type': 'game',
    'date': '',
    'score': '',
    'rules violations': [
		{
            'card': '',
			'name': '',
            'minute': '',
            'reason': ''
		}
    ],
    'goals': [
		{
			'name': '',
            'position': '',
            'minute': '',
            'pass': ''
		}
	],
    'penalties': [
		{
			'name': '',
            'position': '',
            'minute': '',
            'pass': ''
		}
	],
    'shots number on goal': [
		{
			'name': '',
            'position': '',
            'minute': '',
            'pass': ''
		}
	]
}

team1 = {
    'type': 'team',
    'name': 'Работяги',
    'city': 'Петрозаводск',
    'coach name': 'Жмашенко В. Н.', 
    'players': [
        {'name': 'Смирнов П. П.', 'position': 1},
        {'name': 'Семёнов Р. А.', 'position': 2},
        {'name': 'Иванов И. И.', 'position': 3},
        {'name': 'Петров П. П.', 'position': 4},
        {'name': 'Кириешкин Л. Р.', 'position': 5},
        {'name': 'Чипсиков М. Р.', 'position': 6},
        {'name': 'Туманян М. М.', 'position': 7},
        {'name': 'Огузков О. О.', 'position': 8},
        {'name': 'Белов Б. Б.', 'position': 9},
        {'name': 'Симагин П. А.', 'position': 10},
        {'name': 'Лукашенко О. Я.', 'position': 11}
    ],
    'reserve players': ['Чурков М. А.', 'Заенко П. Ш.', 'Шиншилин Р. С.', 'Битый А. А.']
}
team2 = {
    'type': 'team',
    'name': 'Пляска',
    'city': 'Костомукша',
    'coach name': 'Жмашенко В. Н.', 
    'players': [
        {'name': 'Кузнецов Игорь Арсеньевич', 'position': 1},
        {'name': 'Аксёнов Павел Филатович', 'position': 2},
        {'name': 'Гаврилов Петр Анатольевич', 'position': 3},
        {'name': 'Одинцов Ефрем Павлович', 'position': 4},
        {'name': 'Кулаков Соломон Даниилович', 'position': 5},
        {'name': 'Юдин Аввакум Всеволодович', 'position': 6},
        {'name': 'Сафонов Велорий Иосифович', 'position': 7},
        {'name': 'Русаков Климент Геннадиевич', 'position': 8},
        {'name': 'Киселёв Александр Эдуардович', 'position': 9},
        {'name': 'Гришин Алан Евгеньевич', 'position': 10},
        {'name': 'Соловьёв Аввакуум Даниилович', 'position': 11}
    ],
    'reserve players': ['Журавлёв Иннокентий Иринеевич', 'Бобров Марк Федосеевич', 'Вишняков Остап Германнович', 'Петров Самуил Константинович']
}

game = {
    'type': 'game',
    'date': '11.09.2023',
    'score': '0:2',
    'team1': "Пляска",
    'team2': "Работяги",
    'rules violations': [
		{'card': 'yellow', 'name': 'Петров П. П.', 'minute': 12, 'reason': 'Касание руками мяча'}
    ],
    'goals': [
		{'name': 'Туманян М. М.', 'position': 7, 'minute': 3, 'pass': 'Дальний пас'},
        {'name': 'Огузков О. О.', 'position': 8, 'minute': 8, 'pass': 'Короткий пас'}
	],
    'penalties': [
		{'name': 'Лукашенко О. Я.','position': 11,'minute': 20, 'pass': 'От стены'}
	]
}

collection.delete_many({})
collection.insert_many([team1, team2])
collection.insert_one(game)

current_document = {}

def show_documents():
    documents = collection.find()
    listbox.delete(0, tk.END)
    for doc in documents:
        print(doc)
        listbox.insert(tk.END, doc)

def save_document():
    collection.insert_one(current_document)
    current_document.clear()

def add_key_value():
    key = key_entry.get()
    value = value_entry.get()
    parts = key.split('.')
    d = current_document
    for part in parts[0:-1]:
        if d.get(part) == None:
            d[part] = {}
        d = d[part]

    d[parts[-1]] = value
    key_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)

def create_text(label, row):
    label = tk.Label(root, text = label)
    label.grid(row=row, column=0)
    text = tk.Entry(root)
    text.grid(row=row, column=1)
    return (label, text)

def execute_query():
    key = key_query_entry.get()
    operator = operator_query_entry.get()
    value = value_query_entry.get()
    if str.isnumeric(value):
        value = int(value)

    if operator == ">":
        documents = collection.find({key: {"$gt": value}})
    elif operator == ">=":
        documents = collection.find({key: {"$gte": value}})
    elif operator == "=":
        documents = collection.find({key: value})
    elif operator == "<=":
        documents = collection.find({key: {"$lte": value}})
    elif operator == "<":
        documents = collection.find({key: {"$lt": value}})
    listbox.delete(0, tk.END)
    for doc in documents:
        listbox.insert(tk.END, doc)

def execute_aggregation():
    command = command_entry.get()
    [verb, agg_key, key, operator, value] = command.split()
    if str.isnumeric(value):
        value = int(value)
    
    if operator == ">":
        filter = {"$gt": value}
    elif operator == ">=":
        filter = {"$gte": value}
    elif operator == "=":
        filter = value
    elif operator == "<=":
        filter = {"$lte": value}
    elif operator == "<":
        filter = {"$lt": value}
    result = collection.aggregate([{'$unwind': '$' + agg_key}, {"$match" : {key : filter}}, {f'${verb}': agg_key}])
    listbox.delete(0, tk.END)
    for doc in result:
        listbox.insert(tk.END, doc)

# Создание графического интерфейса приложения
root = tk.Tk()
root.title("Русы против ящеров")
root.geometry("1920x1080")
root.configure(bg="#FFFFFF")  # Фоновый цвет окна

# Поля ввода и кнопки для добавления ключ-значение
[key_label, key_entry] = create_text("Ключ", 0)
key_label.grid(row=0, column=0, padx=10, pady=10)
key_entry.grid(row=0, column=1, padx=10, pady=10)

[value_label, value_entry] = create_text("Значение", 1)
value_label.grid(row=1, column=0, padx=10, pady=10)
value_entry.grid(row=1, column=1, padx=10, pady=10)

# Кнопка для добавления ключ-значение
add_button = tk.Button(root, text="Добавить ключ-значение", command=add_key_value, font=("Helvetica", 12), bg="#4CAF50", fg="white")
add_button.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

# Кнопка для сохранения документа
save_button = tk.Button(root, text="Сохранить документ", command=save_document, font=("Helvetica", 12), bg="#008CBA", fg="white")
save_button.grid(row=0, column=3, rowspan=2, padx=10, pady=10)

# Кнопка для отображения документов
show_button = tk.Button(root, text="Показать документы", command=show_documents, font=("Helvetica", 12), bg="#FF9800", fg="white")
show_button.grid(row=0, column=4, rowspan=2, padx=10, pady=10)

# Поле для отображения списка документов
listbox = tk.Listbox(root, font=("Helvetica", 12), bg="#E0E0E0", fg="#333333")
listbox.grid(row=2, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

# Поля ввода, кнопка и список для выполнения запроса на поиск данных
[key_query_label, key_query_entry] = create_text("Ключ для поиска", 3)
[operator_query_label, operator_query_entry] = create_text('Оператор для поиска', 4)
[value_query_label, value_query_entry] = create_text('Значение для поиска', 5)

query_button = tk.Button(root, text="Выполнить запрос", command=execute_query, font=("Helvetica", 12), bg="#FF5722", fg="white")
query_button.grid(row=6, column=0, columnspan=5, padx=10, pady=10)

# Поля ввода, кнопка и список для выполнения агрегации данных
[command_label, command_entry] = create_text('Команда для агрегации', 7)

aggregation_button = tk.Button(root, text="Выполнить агрегацию", command=execute_aggregation, font=("Helvetica", 12), bg="#795548", fg="white")
aggregation_button.grid(row=8, column=0, columnspan=5, padx=10, pady=10)

root.mainloop()