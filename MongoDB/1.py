from pymongo import MongoClient
from tkinter import *
from tkinter.ttk import *
import copy


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
        {'name': 'Смирнов П. П.', 'position': '1'},
        {'name': 'Семёнов Р. А.', 'position': '2'},
        {'name': 'Иванов И. И.', 'position': '3'},
        {'name': 'Петров П. П.', 'position': '4'},
        {'name': 'Кириешкин Л. Р.', 'position': '5'},
        {'name': 'Чипсиков М. Р.', 'position': '6'},
        {'name': 'Туманян М. М.', 'position': '7'},
        {'name': 'Огузков О. О.', 'position': '8'},
        {'name': 'Белов Б. Б.', 'position': '9'},
        {'name': 'Симагин П. А.', 'position': '10'},
        {'name': 'Лукашенко О. Я.', 'position': '11'}
    ],
    'reserve players': ['Чурков М. А.', 'Заенко П. Ш.', 'Шиншилин Р. С.', 'Битый А. А.']
}
team2 = {
    'type': 'team',
    'name': 'Пляска',
    'city': 'Костомукша',
    'coach name': 'Жмашенко В. Н.', 
    'players': [
        {'name': 'Кузнецов Игорь Арсеньевич', 'position': '1'},
        {'name': 'Аксёнов Павел Филатович', 'position': '2'},
        {'name': 'Гаврилов Петр Анатольевич', 'position': '3'},
        {'name': 'Одинцов Ефрем Павлович', 'position': '4'},
        {'name': 'Кулаков Соломон Даниилович', 'position': '5'},
        {'name': 'Юдин Аввакум Всеволодович', 'position': '6'},
        {'name': 'Сафонов Велорий Иосифович', 'position': '7'},
        {'name': 'Русаков Климент Геннадиевич', 'position': '8'},
        {'name': 'Киселёв Александр Эдуардович', 'position': '9'},
        {'name': 'Гришин Алан Евгеньевич', 'position': '10'},
        {'name': 'Соловьёв Аввакуум Даниилович', 'position': '11'}
    ],
    'reserve players': ['Журавлёв Иннокентий Иринеевич', 'Бобров Марк Федосеевич', 'Вишняков Остап Германнович', 'Петров Самуил Константинович']
}

game = {
    'type': 'game',
    'date': '11.09.2023',
    'score': '1:3',
    'rules violations': [
		{'card': 'yellow', 'name': 'Петров П. П.', 'minute': '12', 'reason': 'Касание руками мяча'}
    ],
    'goals': [
		{'name': 'Туманян М. М.', 'position': '7', 'minute': '3', 'pass': 'Дальний пас'},
        {'name': 'Огузков О. О.', 'position': '8', 'minute': '8', 'pass': 'Короткий пас'}
	],
    'penalties': [
		{'name': 'Лукашенко О. Я.','position': '11','minute': '20', 'pass': 'От стены'}
	]
}

collection.delete_many({})
collection.insert_one(team1)
collection.insert_one(team2)
collection.insert_one(game)

current_document = copy.deepcopy(pattern_team)

root = Tk()
root.title('Придумай потом что-нибудь')
root.geometry('900x550')

value_label = Label(text='Введите ключ-значение (например: players.0.name = Сидоров Л. Л.)')
value_label.place(x=20, y=20)
value_entry = Text()
value_entry.place(x=20, y=50, width=320, height=120)

documents_text = Text()
documents_text.place(x=20, y=180, width=960, height=550)
documents_text.configure(state=DISABLED)

def update_documents_text():
    global current_document
    documents_text.configure(state=NORMAL)
    documents_text.delete('1.0', END)
    documents_text.insert(1.0, current_document)
    documents_text.configure(state=DISABLED)

document_type_selection_combobox = Combobox(values=['Teams', 'Games'], state="readonly")
document_type_selection_combobox.place(x=350, y=50)
document_type_selection_combobox.current(newindex=0)

def switch_document_type(event):
    global current_document
    if (document_type_selection_combobox.get() == 'Teams'):
        current_document.clear()
        current_document = copy.deepcopy(pattern_team)
    else:
        current_document.clear()
        current_document = copy.deepcopy(pattern_game)
    update_documents_text()

document_type_selection_combobox.bind('<<ComboboxSelected>>', switch_document_type)

def add_value():
    key_value = value_entry.get(1.0, END).split(' = ')
    key = key_value[0].split('.')
    value = key_value[1].replace('\n', '')
    keys_number = len(key)
    global current_document
    match keys_number:
        case 1:
            current_document[key[0]] = value
        case 2: 
            try:
                current_document[key[0]][int(key[1])] = value
            except IndexError:
                current_document[key[0]].append('')
                current_document[key[0]][int(key[1])] = value
        case 3: 
            try:
                current_document[key[0]][int(key[1])][key[2]] = value
            except IndexError:
                if (key[0] == 'players'):
                    current_document[key[0]].append({ 'name': '', 'position': '' })
                    current_document[key[0]][int(key[1])][key[2]] = value
                elif (key[0] == 'rules violations'):
                    current_document[key[0]].append({ 'card': '', 'name': '', 'minute': '', 'reason': '' })
                    current_document[key[0]][int(key[1])][key[2]] = value
                else:
                    current_document[key[0]].append({ 'name': '', 'position': '', 'minute': '', 'pass': '' })
                    current_document[key[0]][int(key[1])][key[2]] = value
    update_documents_text()

add_key_value_button = Button(text='Добавить значение', command=add_value)
add_key_value_button.place(x=350, y=140, width=110, height=30)

def save_document():
    collection.insert_one(current_document)
    show_documents()

save_documents_button = Button(text='Сохранить документ', command=save_document)
save_documents_button.place(x=470, y=140, width=110, height=30)

def show_documents():
    documents = ''
    for document in collection.find({}, {'_id': 0}):
        documents += str(f"Игра: {document}" if document["type"] == "game" else f"Команда: {document}") + '\n\n'
    documents_text.configure(state=NORMAL)
    documents_text.delete('1.0', END)
    documents_text.insert(1.0, documents)
    documents_text.configure(state=DISABLED)

show_documents_button = Button(text='Показать документы', command=show_documents)
show_documents_button.place(x=590, y=140, width=110, height=30)

root.mainloop()

client.close()