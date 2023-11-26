from pymongo import MongoClient
from tkinter import *
from tkinter.ttk import *


client = MongoClient('mongodb://192.168.112.103')
db = client['22303']

collection = db['tumanyan']

category_1_item_1 = {
	'product_name': 'набор закладок',
	'manufacturer': 'CENTRUM',
	'price': 264,
	'features': {
		'category': 'канцелярия',
		'colour': 'красный',
		'pcs': '6'
	},
	'buyers': [
		{
			'name': 'Мельникова В. Р.',
			'purchase_date': '03.07.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Ковалева Е. А.',
			'purchase_date': '05.07.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Карэкс'
		}
	]
}
category_1_item_2 = {
	'product_name': 'набор магнитных закладок',
	'manufacturer': 'Орландо',
	'price': 170,
	'features': {
		'category': 'канцелярия',
		'colour': 'синий',
		'pcs': '6'
	},
	'buyers': [
		{
			'name': 'Бородина А. И.',
			'purchase_date': '12.02.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Карэкс'
		},
		{
			'name': 'Ширяев Г. К.',
			'purchase_date': '03.07.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Гусев Я. В.',
			'purchase_date': '13.10.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Федорова Е. В.',
			'purchase_date': '10.10.2021',
			'feedback': 'Отличное качество',
			'delivery_service': 'Карэкс'
		},
		{
			'name': 'Лазарева В. А.',
			'purchase_date': '02.07.2021',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Алексеева А. Л.',
			'purchase_date': '08.03.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Фролов Р. А.',
			'purchase_date': '31.01.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		}
	]
}
category_1_item_3 = {
	'product_name': 'папка А3',
	'manufacturer': 'Пифагор',
	'price': 279,
	'features': {
		'category': 'канцелярия',
		'colour': 'красный',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Щербаков А. М.',
			'purchase_date': '13.07.2021',
			'feedback': 'Плохое качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Ковалева Е. А.',
			'purchase_date': '16.02.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Boxberry'
		},
		{
			'name': 'Дружинин П. А.',
			'purchase_date': '02.07.2022',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Ширяев Г. К.',
			'purchase_date': '09.08.2021',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Щербаков А. М.',
			'purchase_date': '30.09.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Шестаков Л. З.',
			'purchase_date': '15.02.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'СДЭК'
		}
	]
}
category_1_item_4 = {
	'product_name': 'блокнот',
	'manufacturer': 'Орладно',
	'price': 369,
	'features': {
		'category': 'канцелярия',
		'colour': 'cиний',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Елисеев А. Д.',
			'purchase_date': '28.10.2021',
			'feedback': 'Неудовлетворительное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Евдокимов М. А.',
			'purchase_date': '07.04.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Глебов М. С.',
			'purchase_date': '23.09.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Леонтьев А. М.',
			'purchase_date': '02.12.2021',
			'feedback': 'Отличное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Андрианов В. Н.',
			'purchase_date': '31.08.2021',
			'feedback': 'Плохое качество',
			'delivery_service': 'Boxberry'
		},
		{
			'name': 'Алексеева А. Л.',
			'purchase_date': '11.08.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Boxberry'
		}
	]
}
category_1_item_5 = {
	'product_name': 'папка А4',
	'manufacturer': 'Пифагор',
	'price': 249,
	'features': {
		'category': 'канцелярия',
		'colour': 'синий',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Головина М. С.',
			'purchase_date': '07.10.2021',
			'feedback': 'Неудовлетворительное качество',
			'delivery_service': 'Карэкс'
		}
	]
}
category_2_item_1 = {
	'product_name': 'набор обложек для переплета А4',
	'manufacturer': 'Brauberg',
	'price': 490,
	'features': {
		'category': 'полиграфическое оборудование',
		'colour': 'синий',
		'pcs': '100'
	},
	'buyers': [
		{
			'name': 'Акимов Д. И.',
			'purchase_date': '20.07.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'DPD'
		}
	]
}
category_2_item_2 = {
	'product_name': 'набор пружин для переплета 12 мм',
	'manufacturer': 'Brauberg',
	'price': 390,
	'features': {
		'category': 'полиграфическое оборудование',
		'colour': 'белый',
		'pcs': '100'
	},
	'buyers': [
		{
			'name': 'Евдокимов М. А.',
			'purchase_date': '27.02.2022',
			'feedback': 'Плохое качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Булгакова Е. И.',
			'purchase_date': '15.05.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Федорова Е. В.',
			'purchase_date': '15.07.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Новиков А. А.',
			'purchase_date': '30.09.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'Boxberry'
		}
	]
}
category_2_item_3 = {
	'product_name': 'набор пружин для переплета 51 мм',
	'manufacturer': 'Brauberg',
	'price': 990,
	'features': {
		'category': 'полиграфическое оборудование',
		'colour': 'белый',
		'pcs': '50'
	},
	'buyers': [
		{
			'name': 'Елисеев А. Д.',
			'purchase_date': '18.11.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Тарасова Е. М.',
			'purchase_date': '11.12.2021',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'Boxberry'
		},
		{
			'name': 'Кошелева С. А.',
			'purchase_date': '27.07.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Карэкс'
		},
		{
			'name': 'Бородина А. И.',
			'purchase_date': '07.02.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Мельникова В. Р.',
			'purchase_date': '11.07.2021',
			'feedback': 'Неудовлетворительное качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Андрианов В. Н.',
			'purchase_date': '27.09.2022',
			'feedback': 'Неудовлетворительное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Иванов К. Я.',
			'purchase_date': '25.08.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Boxberry'
		}
	]
}
category_2_item_4 = {
	'product_name': 'картридж LC985M',
	'manufacturer': 'Brother',
	'price': 738,
	'features': {
		'category': 'полиграфическое оборудование',
		'colour': 'черный',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Евдокимов М. А.',
			'purchase_date': '01.11.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'Boxberry'
		},
		{
			'name': 'Дружинина О. Д.',
			'purchase_date': '20.09.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Глебов М. С.',
			'purchase_date': '03.10.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Гусев Я. В.',
			'purchase_date': '16.10.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'КИТ'
		}
	]
}
category_2_item_5 = {
	'product_name': 'картридж LC1000M',
	'manufacturer': 'Brother',
	'price': 1044,
	'features': {
		'category': 'полиграфическое оборудование',
		'colour': 'черный',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Головина М. С.',
			'purchase_date': '01.08.2021',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Акимов Д. И.',
			'purchase_date': '29.03.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		}
	]
}
category_3_item_1 = {
	'product_name': 'пульт для проектора NEC NP-M230XG',
	'manufacturer': 'NEC',
	'price': 1440,
	'features': {
		'category': 'оборудование для презентаций',
		'colour': 'белый',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Кошелева С. А.',
			'purchase_date': '03.10.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Елисеев А. Д.',
			'purchase_date': '04.09.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Акимов Д. И.',
			'purchase_date': '31.10.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Boxberry'
		},
		{
			'name': 'Гусев Я. В.',
			'purchase_date': '12.01.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'КИТ'
		}
	]
}
category_3_item_2 = {
	'product_name': 'ремешок для проектора Xgimi CC',
	'manufacturer': 'XGIMI',
	'price': 1197,
	'features': {
		'category': 'оборудование для презентаций',
		'colour': 'черный',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Еремина Н. А.',
			'purchase_date': '30.07.2021',
			'feedback': 'Отличное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Ширяев Г. К.',
			'purchase_date': '19.08.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Акимов Д. И.',
			'purchase_date': '12.10.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Андрианов В. Н.',
			'purchase_date': '01.08.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Карэкс'
		},
		{
			'name': 'Щеглова Л. П.',
			'purchase_date': '24.02.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Андрианов В. Н.',
			'purchase_date': '30.06.2022',
			'feedback': 'Неудовлетворительное качество',
			'delivery_service': 'Карэкс'
		},
		{
			'name': 'Леонтьев А. М.',
			'purchase_date': '27.10.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'DPD'
		}
	]
}
category_3_item_3 = {
	'product_name': 'проектор Canon LV-X320',
	'manufacturer': 'Canon',
	'price': 31830,
	'features': {
		'category': 'оборудование для презентаций',
		'colour': 'белый',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Ковалева Е. А.',
			'purchase_date': '06.08.2021',
			'feedback': 'Плохое качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Фролов Р. А.',
			'purchase_date': '29.04.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'СДЭК'
		}
	]
}
category_3_item_4 = {
	'product_name': 'проектор Canon LV-WX320',
	'manufacturer': 'Canon',
	'price': 34560,
	'features': {
		'category': 'оборудование для презентаций',
		'colour': 'черный',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Еремина Н. А.',
			'purchase_date': '19.07.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Бородина А. И.',
			'purchase_date': '13.09.2021',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Булгакова Е. И.',
			'purchase_date': '01.07.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'КИТ'
		}
	]
}
category_3_item_5 = {
	'product_name': 'пульт для проектора ViewSonic PJD7820HD',
	'manufacturer': 'Scw',
	'price': 1600,
	'features': {
		'category': 'оборудование для презентаций',
		'colour': 'черный',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Глебов М. С.',
			'purchase_date': '14.08.2021',
			'feedback': 'Плохое качество',
			'delivery_service': 'Boxberry'
		},
		{
			'name': 'Алексеева Д. Р.',
			'purchase_date': '10.09.2021',
			'feedback': 'Отличное качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Головина М. С.',
			'purchase_date': '17.07.2021',
			'feedback': 'Неудовлетворительное качество',
			'delivery_service': 'Карэкс'
		}
	]
}
category_4_item_1 = {
	'product_name': 'этикет-лента 21x12 мм прямоугольная',
	'manufacturer': 'Brauberg',
	'price': 10,
	'features': {
		'category': 'оргтехника',
		'colour': 'белый',
		'pcs': '3000'
	},
	'buyers': [
		{
			'name': 'Ширяев Г. К.',
			'purchase_date': '06.10.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Карэкс'
		}
	]
}
category_4_item_2 = {
	'product_name': 'картридж ProMega Print 106R01602',
	'manufacturer': 'ProMega',
	'price': 11,
	'features': {
		'category': 'оргтехника',
		'colour': 'синий',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Леонтьев А. М.',
			'purchase_date': '21.12.2021',
			'feedback': 'Отличное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Елисеев А. Д.',
			'purchase_date': '29.10.2022',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'Карэкс'
		},
		{
			'name': 'Глебов М. С.',
			'purchase_date': '18.08.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Евдокимов М. А.',
			'purchase_date': '15.11.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Фролов Р. А.',
			'purchase_date': '04.01.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Boxberry'
		},
		{
			'name': 'Дружинин П. А.',
			'purchase_date': '07.08.2021',
			'feedback': 'Неудовлетворительное качество',
			'delivery_service': 'DPD'
		},
		{
			'name': 'Тарасова Е. М.',
			'purchase_date': '05.09.2021',
			'feedback': 'Отличное качество',
			'delivery_service': 'Boxberry'
		}
	]
}
category_4_item_3 = {
	'product_name': 'лента Epson LC-5SBR1 C53S626414',
	'manufacturer': 'Epson',
	'price': 25,
	'features': {
		'category': 'оргтехника',
		'colour': 'черный',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Кошелева С. А.',
			'purchase_date': '22.08.2021',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'КИТ'
		},
		{
			'name': 'Никифоров Е. М.',
			'purchase_date': '14.02.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Boxberry'
		}
	]
}
category_4_item_4 = {
	'product_name': 'картридж матричный Cactus CS-ERC31',
	'manufacturer': 'Cactus',
	'price': 45,
	'features': {
		'category': 'оргтехника',
		'colour': 'черный',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Егорова С. А.',
			'purchase_date': '17.09.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Шестаков Л. З.',
			'purchase_date': '28.01.2022',
			'feedback': 'Отличное качество',
			'delivery_service': 'СДЭК'
		},
		{
			'name': 'Тарасова Е. М.',
			'purchase_date': '22.07.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Boxberry'
		}
	]
}
category_4_item_5 = {
	'product_name': 'тонер Cactus CS-THP7C-45',
	'manufacturer': 'Cactus',
	'price': 45,
	'features': {
		'category': 'оргтехника',
		'colour': 'белый',
		'pcs': '1'
	},
	'buyers': [
		{
			'name': 'Никифоров Е. М.',
			'purchase_date': '09.07.2021',
			'feedback': 'Удовлетворительное качество',
			'delivery_service': 'Карэкс'
		},
		{
			'name': 'Шестаков Л. З.',
			'purchase_date': '15.10.2022',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Карэкс'
		},
		{
			'name': 'Щеглова Л. П.',
			'purchase_date': '24.12.2021',
			'feedback': 'Хорошее качество',
			'delivery_service': 'Boxberry'
		}
	]
}

collection.delete_many({})
collection.insert_many(
	[
		category_1_item_1,
		category_1_item_2,
		category_1_item_3,
		category_1_item_4,
		category_1_item_5,
		category_2_item_1,
		category_2_item_2,
		category_2_item_3,
		category_2_item_4,
		category_2_item_5,
		category_3_item_1,
		category_3_item_2,
		category_3_item_3,
		category_3_item_4,
		category_3_item_5,
		category_4_item_1,
		category_4_item_2,
		category_4_item_3,
		category_4_item_4,
		category_4_item_5
	]
)

root = Tk()
root.title('DB2 Lab2.4')
root.geometry('800x600')

queries_combobox_values = [
	'Получить список названий товаров, относящихся к заданной категории',
	'Получить список характеристик товаров заданной категории',
	'Получить список названий и стоимости товаров, купленных заданным покупателем',
	'Получить список названий, производителей и цен на товары, имеющие заданный цвет',
	'Получить общую сумму проданных товаров',
	'Получить количество товаров в каждой категории',
	'Получить список имен покупателей заданного товара',
	'Получить список имен покупателей заданного товара, с доставкой фирмы с заданным названием'
]
queries_combobox = Combobox(values=queries_combobox_values, state='readonly')
queries_combobox.place(x=20, y=20, width=600)

product_categories_values = [
	'канцелярия',
	'полиграфическое оборудование',
	'оборудование для презентаций',
	'оргтехника'
]
product_categories_combobox = Combobox(values=product_categories_values, state='disabled')
product_categories_combobox.place(x=20, y=60, width=600)
product_categories_combobox.current(newindex=0)

buyers_values = [
	'Мельникова В. Р.',
	'Кошелева С. А.',
	'Бородина А. И.',
	'Головина М. С.',
	'Еремина Н. А.',
	'Алексеева Д. Р.',
	'Ковалева Е. А.',
	'Глебов М. С.',
	'Фролов Р. А.',
	'Акимов Д. И.',
	'Евдокимов М. А.',
	'Елисеев А. Д.',
	'Ширяев Г. К.',
	'Щербаков А. М.',
	'Дружинин П. А.',
	'Дружинина О. Д.',
	'Булгакова Е. И.',
	'Лазарева В. А.',
	'Гусев Я. В.',
	'Алексеева А. Л.',
	'Федорова Е. В.',
	'Тарасова Е. М.',
	'Леонтьев А. М.',
	'Шестаков Л. З.',
	'Андрианов В. Н.',
	'Никифоров Е. М.',
	'Новиков А. А.',
	'Егорова С. А.',
	'Иванов К. Я.',
	'Щеглова Л. П.'
]
buyers_combobox = Combobox(values=buyers_values, state='disabled')
buyers_combobox.place(x=20, y=100, width=600)
buyers_combobox.current(newindex=0)

product_colours_values = [
	'черный',
	'белый',
	'синий',
	'красный'
]
product_colours_combobox = Combobox(values=product_colours_values, state='disabled')
product_colours_combobox.place(x=20, y=140, width=600)
product_colours_combobox.current(newindex=0)

product_names_values = [
	'набор закладок',
	'набор магнитных закладок',
	'папка А3',
	'блокнот',
	'папка А4',
	'набор обложек для переплета А4',
	'набор пружин для переплета 12 мм',
	'набор пружин для переплета 51 мм',
	'картридж LC985M',
	'картридж LC1000M',
	'пульт для проектора NEC NP-M230XG',
	'ремешок для проектора Xgimi CC',
	'проектор Canon LV-X320',
	'проектор Canon LV-WX320',
	'пульт для проектора ViewSonic PJD7820HD',
	'этикет-лента 21x12 мм прямоугольная',
	'картридж ProMega Print 106R01602',
	'лента Epson LC-5SBR1 C53S626414',
	'картридж матричный Cactus CS-ERC31',
	'тонер Cactus CS-THP7C-45'
]
product_names_combobox = Combobox(values=product_names_values, state='disabled')
product_names_combobox.place(x=20, y=180, width=600)
product_names_combobox.current(newindex=0)

delivery_services_values = [
	'КИТ',
	'СДЭК',
	'Boxberry',
	'DPD',
	'Карэкс',
]
delivery_services_combobox = Combobox(values=delivery_services_values, state='disabled')
delivery_services_combobox.place(x=20, y=220, width=600)
delivery_services_combobox.current(newindex=0)

result_table = Treeview(columns=('1', '2', '3'), show='headings')
result_table.place(x=20, y=260)

def task_1():
	result_table.delete(*result_table.get_children())
	for e in collection.aggregate([
		{'$match': {'features.category': product_categories_combobox.get()}}, 
		{'$replaceRoot': {'newRoot': {'product_name': '$product_name'}}}
	]):
		result_table.insert('', 'end', values=list(e.values()))

def task_2():
	result_table.delete(*result_table.get_children())
	for e in collection.aggregate([
		{'$match': {'features.category': product_categories_combobox.get()}},
        {'$replaceRoot': {'newRoot': {'product_name': '$product_name', 'colour': '$features.colour', 'pcs': '$features.pcs'}}}
	]):
		values_list = list(e.values())
		values_list[2] += ' шт.'
		result_table.insert('', 'end', values=values_list)

def task_3():
	result_table.delete(*result_table.get_children())
	for e in collection.aggregate([
		{'$match': {'buyers.name': buyers_combobox.get()}},
        {'$replaceRoot': {'newRoot': {'product_name': '$product_name', 'price': '$price'}}}
	]):
		values_list = list(e.values())
		values_list[1] = str(values_list[1]) + ' руб.'
		result_table.insert('', 'end', values=values_list)

def task_4():
	result_table.delete(*result_table.get_children())
	for e in collection.aggregate([
		{'$match': {'features.colour': product_colours_combobox.get()}},
        {'$replaceRoot': {'newRoot': {'product_name': '$product_name', 'manufacturer': '$manufacturer', 'price': '$price'}}}
	]):
		values_list = list(e.values())
		values_list[2] = str(values_list[2]) + ' руб.'
		result_table.insert('', 'end', values=values_list)

def task_5():
	result_table.delete(*result_table.get_children())
	for e in collection.aggregate([
		{'$group': {'_id': 'null', 'sum_val': {'$sum': {'$multiply': ['$price', {'$size': '$buyers'}]}}}},
        {'$replaceRoot': {'newRoot': {'sum_val': '$sum_val'}}}
	]):
		values_list = list(e.values())
		values_list[0] = str(values_list[0]) + ' руб.'
		result_table.insert('', 'end', values=values_list)

def task_6():
	result_table.delete(*result_table.get_children())
	for e in collection.aggregate([
		{'$group': {'_id': '$features.category', 'count': {'$sum': 1}}},
        {'$replaceRoot': {'newRoot': {'category': '$_id', 'count': '$count'}}}
	]):
		result_table.insert('', 'end', values=list(e.values()))

def task_7():
	result_table.delete(*result_table.get_children())
	for e in collection.aggregate([
		{'$unwind': '$buyers'},
        {'$match': {'product_name': product_names_combobox.get()}},
        {'$replaceRoot': {'newRoot': {'name': '$buyers.name'}}}
	]):
		result_table.insert('', 'end', values=list(e.values()))

def task_8():
	result_table.delete(*result_table.get_children())
	for e in collection.aggregate([
		{'$unwind': '$buyers'},
        {'$match': {'buyers.delivery_service': delivery_services_combobox.get(), 'product_name': product_names_combobox.get()}},
        {'$replaceRoot': {'newRoot': {'name': '$buyers.name'}}}
	]):
		result_table.insert('', 'end', values=list(e.values()))

comboboxes = [		
	product_categories_combobox, 
	buyers_combobox, 
	product_colours_combobox,
	product_names_combobox,
	delivery_services_combobox
]

def activate_comboboxes(comboboxes_to_activate: list):
	for combobox in comboboxes:
		if (combobox in comboboxes_to_activate):
			combobox.configure(state='readonly')
		else:
			combobox.configure(state='disabled')

def switch_arguments_and_send_query(event):
	comboboxes_to_activate = []
	selected_query_number = queries_combobox.current()
	if (selected_query_number == 0):
		comboboxes_to_activate.clear()
		comboboxes_to_activate.append(product_categories_combobox)
		activate_comboboxes(comboboxes_to_activate)
		task_1()
	elif (selected_query_number == 1):
		comboboxes_to_activate.clear()
		comboboxes_to_activate.append(product_categories_combobox)
		activate_comboboxes(comboboxes_to_activate)
		task_2()
	elif (selected_query_number == 2):
		comboboxes_to_activate.clear()
		comboboxes_to_activate.append(buyers_combobox)
		activate_comboboxes(comboboxes_to_activate)
		task_3()
	elif (selected_query_number == 3):
		comboboxes_to_activate.clear()
		comboboxes_to_activate.append(product_colours_combobox)
		activate_comboboxes(comboboxes_to_activate)
		task_4()
	elif (selected_query_number == 4):
		comboboxes_to_activate.clear()
		activate_comboboxes(comboboxes_to_activate)
		task_5()
	elif (selected_query_number == 5):
		comboboxes_to_activate.clear()
		activate_comboboxes(comboboxes_to_activate)
		task_6()
	elif (selected_query_number == 6):
		comboboxes_to_activate.clear()
		comboboxes_to_activate.append(product_names_combobox)
		activate_comboboxes(comboboxes_to_activate)
		task_7()
	elif (selected_query_number == 7):
		comboboxes_to_activate.clear()
		comboboxes_to_activate.append(product_names_combobox)
		comboboxes_to_activate.append(delivery_services_combobox)
		activate_comboboxes(comboboxes_to_activate)
		task_8()

queries_combobox.bind('<<ComboboxSelected>>', switch_arguments_and_send_query)

def update_result_table(event):
	selected_query_number = queries_combobox.current()
	if (selected_query_number == 0):
		task_1()
	elif (selected_query_number == 1):
		task_2()
	elif (selected_query_number == 2):
		task_3()
	elif (selected_query_number == 3):
		task_4()
	elif (selected_query_number == 4):
		task_5()
	elif (selected_query_number == 5):
		task_6()
	elif (selected_query_number == 6):
		task_7()
	elif (selected_query_number == 7):
		task_8()

for combobox in comboboxes:
	combobox.bind('<<ComboboxSelected>>', update_result_table)

root.mainloop()

client.close()