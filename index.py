import telebot
from telebot import *
import datetime
import threading
import pickle
import re
import schedule


global megaadmins
megaadmins = [1343852948, 514367287]

try:
    with open("grafiky.pkl", "rb") as file:
        grafiky_kategory = pickle.load(file)
except FileNotFoundError:
    grafiky_kategory = []



# Функция для добавления продукта в список
def add_grafiky_kategory(grafiky_punkt):
    grafiky_kategory.append(grafiky_punkt)
    print(f"Продукт '{grafiky_punkt}' успешно добавлен.")
    save_grafiky_file_kat()


# Функция для обновления продукта
def update_grafiky_kategory(old_grafiky_punkt, new_grafiky_punkt):
    if old_grafiky_punkt in grafiky_kategory:
        grafiky_index = grafiky_kategory.index(old_grafiky_punkt)
        grafiky_kategory[grafiky_index] = new_grafiky_punkt
        print(f"Продукт '{old_grafiky_punkt}' успешно обновлен на '{new_grafiky_punkt}'.")
        save_grafiky_file_kat()
    else:
        print(f"Продукт '{old_grafiky_punkt}' не найден в списке.")


# Функция для удаления продукта
def remove_grafiky_kategory(grafiky_punkt):
    if grafiky_punkt in grafiky_kategory:
        grafiky_kategory.remove(grafiky_punkt)
        print(f"Продукт '{grafiky_punkt}' успешно удален.")
        save_grafiky_file_kat()
    else:
        print(f"Продукт '{grafiky_punkt}' не найден в списке.")


# Функция для вывода всех продуктов
def show_grafiky_kategory():
    if grafiky_kategory:
        grafiky_pokaz_kat = "\n".join(grafiky_punkt for grafiky_punkt in grafiky_kategory)
        return grafiky_pokaz_kat
        for grafiky_punkt in grafiky_kategory:
            print(f"Продукт: {grafiky_punkt}")
    else:
        print("Список продуктов пуст.")

# Функция для сохранения данных в файл
def save_grafiky_file_kat():
    with open("grafiky.pkl", "wb") as file:
        pickle.dump(grafiky_kategory, file)

# При загрузке данных из файла
def load_grafiky_file_kat():
    try:
        with open("grafiky.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# При загрузке переменной selected_numbers из файла pickle
def load_selected_numbers():
    selected_numbers = {}
    for grafik in grafiky_kategory:
        parts = grafik.split("|")
        for part in parts[1:]:
            day, numbers = part.split(":")
            selected_numbers[day.strip()] = [num.strip() for num in numbers.split(",")]
    return selected_numbers

# При сохранении переменной selected_numbers в файл pickle
def save_selected_numbers(selected_numbers):
    selected_numbers_list = []
    for day, numbers in selected_numbers.items():
        numbers_str = ", ".join(numbers)
        selected_numbers_list.append(f"{day}: {numbers_str}")
    grafiky_kategory.append("|".join(selected_numbers_list))
    save_grafiky_file_kat()

# Функция для обновления переменной selected_numbers
def update_selected_numbers(old_selected_numbers, new_selected_numbers):
    old_selected_numbers.update(new_selected_numbers)
    save_selected_numbers(old_selected_numbers)

# При запуске программы загружаем данные из файлов
grafiky_kategory = load_grafiky_file_kat()
selected_numbers = load_selected_numbers()

# Далее в коде мы будем использовать переменные grafiky_kategory и selected_numbers
# вместо жестко заданных значений, чтобы работать с сохраненными данными.














try:
    with open("workers.pkl", "rb") as file:
        workers_kategory = pickle.load(file)
except FileNotFoundError:
    workers_kategory = []


# Функция для добавления продукта в список
def add_workers_kategory(workers_punkt):
    workers_kategory.append(workers_punkt)
    print(f"Продукт '{workers_punkt}' успешно добавлен.")
    save_workers_file_kat()


# Функция для обновления продукта
def update_workers_kategory(old_workers_punkt, new_workers_punkt):
    if old_workers_punkt in workers_kategory:
        workers_index = workers_kategory.index(old_workers_punkt)
        workers_kategory[workers_index] = new_workers_punkt
        print(f"Продукт '{old_workers_punkt}' успешно обновлен на '{new_workers_punkt}'.")
        save_workers_file_kat()
    else:
        print(f"Продукт '{old_workers_punkt}' не найден в списке.")


# Функция для удаления продукта
def remove_workers_kategory(workers_punkt):
    if workers_punkt in workers_kategory:
        workers_kategory.remove(workers_punkt)
        print(f"Продукт '{workers_punkt}' успешно удален.")
        save_workers_file_kat()
    else:
        print(f"Продукт '{workers_punkt}' не найден в списке.")


# Функция для вывода всех продуктов
def show_workers_kategory():
    if workers_kategory:
        workers_pokaz_kat = "\n".join(workers_punkt for workers_punkt in workers_kategory)
        return workers_pokaz_kat
        for workers_punkt in workers_kategory:
            print(f"Продукт: {workers_punkt}")
    else:
        print("Список продуктов пуст.")


# Функция для сохранения данных в файл
def save_workers_file_kat():
    with open("workers.pkl", "wb") as file:
        pickle.dump(workers_kategory, file)







try:
    with open("admins.pkl", "rb") as file:
        admins_kategory = pickle.load(file)
except FileNotFoundError:
    admins_kategory = []


# Функция для добавления продукта в список
def add_admins_kategory(admins_punkt):
    admins_kategory.append(admins_punkt)
    print(f"Продукт '{admins_punkt}' успешно добавлен.")
    save_admins_file_kat()


# Функция для обновления продукта
def update_admins_kategory(old_admins_punkt, new_admins_punkt):
    if old_admins_punkt in admins_kategory:
        admins_index = admins_kategory.index(old_admins_punkt)
        admins_kategory[admins_index] = new_admins_punkt
        print(f"Продукт '{old_admins_punkt}' успешно обновлен на '{new_admins_punkt}'.")
        save_admins_file_kat()
    else:
        print(f"Продукт '{old_admins_punkt}' не найден в списке.")


# Функция для удаления продукта
def remove_admins_kategory(admins_punkt):
    if admins_punkt in admins_kategory:
        admins_kategory.remove(admins_punkt)
        print(f"Продукт '{admins_punkt}' успешно удален.")
        save_admins_file_kat()
    else:
        print(f"Продукт '{admins_punkt}' не найден в списке.")


# Функция для вывода всех продуктов
def show_admins_kategory():
    if admins_kategory:
        admins_pokaz_kat = "\n".join(admins_punkt for admins_punkt in admins_kategory)
        return admins_pokaz_kat
        for admins_punkt in admins_kategory:
            print(f"Продукт: {admins_punkt}")
    else:
        print("Список продуктов пуст.")


# Функция для сохранения данных в файл
def save_admins_file_kat():
    with open("admins.pkl", "wb") as file:
        pickle.dump(admins_kategory, file)

















try:
    with open("kasy.pkl", "rb") as file:
        kasy_kategory = pickle.load(file)
except FileNotFoundError:
    kasy_kategory = []


# Функция для добавления продукта в список
def add_kasy_kategory(kasy_punkt):
    kasy_kategory.append(kasy_punkt)
    print(f"Продукт '{kasy_punkt}' успешно добавлен.")
    save_kasy_file_kat()


# Функция для обновления продукта
def update_kasy_kategory(old_kasy_punkt, new_kasy_punkt):
    if old_kasy_punkt in kasy_kategory:
        kasy_index = kasy_kategory.index(old_kasy_punkt)
        kasy_kategory[kasy_index] = new_kasy_punkt
        print(f"Продукт '{old_kasy_punkt}' успешно обновлен на '{new_kasy_punkt}'.")
        save_kasy_file_kat()
    else:
        print(f"Продукт '{old_kasy_punkt}' не найден в списке.")


# Функция для удаления продукта
def remove_kasy_kategory(kasy_punkt):
    if kasy_punkt in kasy_kategory:
        kasy_kategory.remove(kasy_punkt)
        print(f"Продукт '{kasy_punkt}' успешно удален.")
        save_kasy_file_kat()
    else:
        print(f"Продукт '{kasy_punkt}' не найден в списке.")


# Функция для вывода всех продуктов
def show_kasy_kategory():
    if kasy_kategory:
        kasy_pokaz_kat = "\n".join(kasy_punkt for kasy_punkt in kasy_kategory)
        return kasy_pokaz_kat
        for kasy_punkt in kasy_kategory:
            print(f"Продукт: {kasy_punkt}")
    else:
        print("Список продуктов пуст.")


# Функция для сохранения данных в файл
def save_kasy_file_kat():
    with open("kasy.pkl", "wb") as file:
        pickle.dump(kasy_kategory, file)
























TOKEN = '6872203027:AAGWv2jLJ1EEAH_1vbDM1a6I421UiaPJ97Q'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_com(message):
	found = False
	for i in admins_kategory:
		if str(message.chat.id) in i:
			found = True
			break
	if found == True:
		adminin(message)
	else:	
		found = False
		for i in workers_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			workerin(message)
		else:	
			bot.send_message(message.chat.id, ' У вас нету доступа в этот кабинет')	


@bot.message_handler(commands=['megaadm'])
def mega_com(message):
	if message.chat.id == 1343852948:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

		item1 = types.KeyboardButton('Отправить кассу')
		item2 = types.KeyboardButton('')
		item3 = types.KeyboardButton('')

		item4 = types.KeyboardButton('Исправить кассу')
		item5 = types.KeyboardButton('Удалить кассу')
		item6 = types.KeyboardButton('')

		item7 = types.KeyboardButton('Показать кассы')
		item8 = types.KeyboardButton('')
		item9 = types.KeyboardButton('')

		item10 = types.KeyboardButton('Добавить сотрудника')
		item11 = types.KeyboardButton('Удалить сотрудника')
		item12 = types.KeyboardButton('')

		item13 = types.KeyboardButton('Показать список сотрудников')
		item14 = types.KeyboardButton('')
		item15 = types.KeyboardButton('')

		item16 = types.KeyboardButton('Добавить админа')
		item17 = types.KeyboardButton('Удалить админа')
		item18 = types.KeyboardButton('')

		item19 = types.KeyboardButton('Показать список админов')

		markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19)
		bot.send_message(message.chat.id, 'Добро пожаловать Создатель', reply_markup=markup)    
	else:
		bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')








def send_dayotchet():
	current_date = datetime.date.today()
	today = datetime.date.today().strftime("%d.%m")
	result = 0
	for i in kasy_kategory:
		if str(today) in i:
			parts = i.split("|")
			result = result + int(parts[4])

	bot.send_message(1343852948, 'Сейчас: 23:00\n\n'+str(today)+'✅\n+'+str(result)+'€')
	



def send_nedelnyotchet():
	bot.send_message(1343852948, 'Сейчас Воскресенье: 23:00')
#########################ЦИКЛИ№#########################
#########################ЦИКЛИ№#########################
#########################ЦИКЛИ№#########################

schedule.every().day.at("23:00").do(send_dayotchet)
schedule.every().sunday.at("23:00").do(send_nedelnyotchet)


# Функция для запуска планировщика в отдельном потоке
def schedule_thread():
    while True:
        schedule.run_pending()


# Создание и запуск отдельного потока для планировщика
schedule_t = threading.Thread(target=schedule_thread)
schedule_t.start()


#########################ЦИКЛИ№#########################
#########################ЦИКЛИ№#########################
#########################ЦИКЛИ№#########################










@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.text == 'Кассы':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin_kasy(message)
		else:	
			bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')
	if message.text == 'Сотрудники':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin_workers(message)
		else:	
			bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')
	if message.text == 'Графики':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin_grafiky(message)
		else:	
			bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')
	if message.text == 'Админы':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin_admins(message)
		else:	
			bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')













	



	if message.text == 'Добавить админа':
		found = False
		for i in megaadmins:
			if str(message.chat.id) in str(i):
				found = True
				break
		if found == True:
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('⬅️Назад')
			markup.add(item1)
			send_add_admin = bot.send_message(message.chat.id, 'Введите айди админа', reply_markup=markup)
			bot.register_next_step_handler(send_add_admin, process_add_admin)
		else:
			pass



	if message.text == 'Добавить сотрудника':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('⬅️Назад')
			markup.add(item1)
			send_add_worker = bot.send_message(message.chat.id, 'Введите айди сотрудника', reply_markup=markup)
			bot.register_next_step_handler(send_add_worker, process_add_worker)
		else:
			pass


	if message.text == 'Удалить сотрудника':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
			for i in workers_kategory:
				parts = i.split("|")
				name = parts[1]

				item_katalog = types.InlineKeyboardButton(name, callback_data='DELW|'+str(i))
				markup_kup_main.add(item_katalog)

			bot.send_message(message.chat.id, 'Выбирите сотрудника', reply_markup=markup_kup_main)
		else:
			pass
	if message.text == 'Удалить админа':
		found = False
		for i in megaadmins:
			if str(message.chat.id) in str(i):
				found = True
				break
		if found == True:
			markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
			for i in admins_kategory:
				parts = i.split("|")
				name = parts[1]

				item_katalog = types.InlineKeyboardButton(name, callback_data='DELA|'+str(i))
				markup_kup_main.add(item_katalog)

			bot.send_message(message.chat.id, 'Выбирите сотрудника', reply_markup=markup_kup_main)
		else:
			pass



	if message.text == 'Исправить кассу':
		up_kasa_tg(message)
	if message.text == 'Удалить кассу':
		del_kasa_tg(message)
		


	if message.text == 'Показать список сотрудников':
		show_workers_tg(message)
	if message.text == 'Показать список админов':
		show_admins_tg(message)
	if message.text == 'Показать кассы':
		show_kasy_tg(message)



	if message.text == 'Мой график':
		found = False
		admorwork = False
		for i in workers_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			admorwork = True
			moj_grafik(message, admorwork)
		else:	
			found = False
			for i in admins_kategory:
				if str(message.chat.id) in i:
					found = True
					break
			if found == True:
				admorwork = False
				moj_grafik(message, admorwork)
			else:
				bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')		


	if message.text == 'Создать мой график':
		found = False
		admorwork = False
		for i in workers_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			admorwork = True
			create_grafik_start(message)
		else:	
			found = False
			for i in admins_kategory:
				if str(message.chat.id) in i:
					found = True
					break
			if found == True:
				admorwork = False
				create_grafik_start(message)
			else:
				bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')

	if message.text == 'Показать мой график':
		found = False
		admorwork = False
		for i in workers_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			admorwork = True
			show_grafik_start(message, admorwork)
		else:	
			found = False
			for i in admins_kategory:
				if str(message.chat.id) in i:
					found = True
					break
			if found == True:
				admorwork = False
				show_grafik_start(message, admorwork)
			else:
				bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')
		
	if message.text == 'Изменить мой график':
		found = False
		admorwork = False
		for i in workers_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			admorwork = True
			up_grafik_start(message)
		else:	
			found = False
			for i in admins_kategory:
				if str(message.chat.id) in i:
					found = True
					break
			if found == True:
				admorwork = False
				up_grafik_start(message)
			else:
				bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')
				

	



	if message.text == 'Показать графики':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			show_grafiky_tg(message)
		else:
			pass


	if message.text == 'Сделать график на завтра':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			do_tomorrow_grakify(message)
		else:
			pass	
		















	if message.text == 'Я Сотрудник':
		found = False
		for i in workers_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			workerin(message)
		else:	
			bot.send_message(message.chat.id, ' У вас нету доступа в этот кабинет')


	if message.text == 'Отправить кассу':
		found = False
		admorwork = False
		for i in workers_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			admorwork = True
			addkasa(message, admorwork)
		else:	
			found = False
			for i in admins_kategory:
				if str(message.chat.id) in i:
					found = True
					break
			if found == True:
				admorwork = False
				addkasa(message, admorwork)
			else:
				bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')







	if message.text == '⬅️Назад':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin(message)
		else:	
			found = False
			for i in workers_kategory:
				if str(message.chat.id) in i:
					found = True
					break
			if found == True:
				workerin(message)
			else:
				bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')










	if message.text == '⬅️Назад к касам':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin_kasy(message)
		else:	
			bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')
	if message.text == '⬅️Назад к сотрудникам':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin_workers(message)
		else:	
			bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')
	if message.text == '⬅️Назад к графикам':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin_grafiky(message)
		else:	
			bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')
	if message.text == '⬅️Назад к админам':
		found = False
		for i in admins_kategory:
			if str(message.chat.id) in i:
				found = True
				break
		if found == True:
			adminin_admins(message)
		else:	
			bot.send_message(message.chat.id, 'У вас нету доступа в этот кабинет')















	


@bot.message_handler(content_types=['text'])
def adminin(message):
	found = False
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	for i in megaadmins:
		if str(message.chat.id) in str(i):
			found = True
			break
	if found == True:
		item1 = types.KeyboardButton('Кассы')
		item2 = types.KeyboardButton('')
		item3 = types.KeyboardButton('')
		item4 = types.KeyboardButton('Сотрудники')
		item5 = types.KeyboardButton('')
		item6 = types.KeyboardButton('')
		item7 = types.KeyboardButton('Графики')
		item8 = types.KeyboardButton('')
		item9 = types.KeyboardButton('')
		item10 = types.KeyboardButton('Витрати')
		item11 = types.KeyboardButton('')
		item12 = types.KeyboardButton('')
		item13 = types.KeyboardButton('Админы')
		item14 = types.KeyboardButton('')
		item15 = types.KeyboardButton('')
		markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15)
	else:
		item1 = types.KeyboardButton('Кассы')
		item2 = types.KeyboardButton('')
		item3 = types.KeyboardButton('')
		item4 = types.KeyboardButton('Сотрудники')
		item5 = types.KeyboardButton('')
		item6 = types.KeyboardButton('')
		item7 = types.KeyboardButton('Графики')
		item8 = types.KeyboardButton('')
		item9 = types.KeyboardButton('')
		item10 = types.KeyboardButton('Витрати')
		item11 = types.KeyboardButton('')
		item12 = types.KeyboardButton('')
		markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)

	
	bot.send_message(message.chat.id, 'Добро пожаловать, Админ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def adminin_kasy(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = types.KeyboardButton('Отправить кассу')
	item2 = types.KeyboardButton('')
	item3 = types.KeyboardButton('')
	item4 = types.KeyboardButton('Исправить кассу')
	item5 = types.KeyboardButton('Удалить кассу')
	item6 = types.KeyboardButton('')
	item7 = types.KeyboardButton('Показать кассы')
	item8 = types.KeyboardButton('')
	item9 = types.KeyboardButton('')
	item10 = types.KeyboardButton('⬅️Назад')
	item11 = types.KeyboardButton('')
	item12 = types.KeyboardButton('')

	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
	bot.send_message(message.chat.id, 'Кабинет: Кассы', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def adminin_workers(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = types.KeyboardButton('Добавить сотрудника')
	item2 = types.KeyboardButton('Удалить сотрудника')
	item3 = types.KeyboardButton('')		
	item4 = types.KeyboardButton('Показать список сотрудников')
	item5 = types.KeyboardButton('')
	item6 = types.KeyboardButton('')
	item7 = types.KeyboardButton('⬅️Назад')
	item8 = types.KeyboardButton('')
	item9 = types.KeyboardButton('')

	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
	bot.send_message(message.chat.id, 'Кабинет: Сотрудники', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def adminin_grafiky(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = types.KeyboardButton('Мой график')
	item2 = types.KeyboardButton('')
	item3 = types.KeyboardButton('')
	item4 = types.KeyboardButton('Показать графики')
	item5 = types.KeyboardButton('')
	item6 = types.KeyboardButton('')
	item7 = types.KeyboardButton('Сделать график на завтра')
	item8 = types.KeyboardButton('')
	item9 = types.KeyboardButton('')
	item10 = types.KeyboardButton('⬅️Назад')
	item11 = types.KeyboardButton('')
	item12 = types.KeyboardButton('')

	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
	bot.send_message(message.chat.id, 'Кабинет: Графики', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def adminin_admins(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = types.KeyboardButton('Добавить админа')
	item2 = types.KeyboardButton('Удалить админа')
	item3 = types.KeyboardButton('')		
	item4 = types.KeyboardButton('Показать список админов')
	item5 = types.KeyboardButton('')
	item6 = types.KeyboardButton('')
	item7 = types.KeyboardButton('⬅️Назад')
	item8 = types.KeyboardButton('')
	item9 = types.KeyboardButton('')

	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
	bot.send_message(message.chat.id, 'Кабинет: Графики', reply_markup=markup)
















@bot.message_handler(content_types=['text'])
def process_add_admin(message):
	if message.text == '⬅️Назад':
		adminin_admins(message)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		adding_admin = str(message.text)
		send_add_admin2 = bot.send_message(message.chat.id, 'Теперь введите его имя', reply_markup=markup)
		bot.register_next_step_handler(send_add_admin2, process_add_admin2, adding_admin)
@bot.message_handler(content_types=['text'])
def process_add_admin2(message, adding_admin):
	if message.text == '⬅️Назад':
		adminin_admins(message)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		adding_name = str(message.text)
		send_add_admin3 = bot.send_message(message.chat.id, 'Введите его @юзернейм', reply_markup=markup)
		bot.register_next_step_handler(send_add_admin3, process_add_admin3, adding_admin, adding_name)
@bot.message_handler(content_types=['text'])
def process_add_admin3(message, adding_admin, adding_name):
	if message.text == '⬅️Назад':
		adminin_admins(message)
	else:
		text = str(adding_admin)+'|'+str(message.text)

		found = False
		for i in admins_kategory:
			if str(adding_admin) in i:
				found = True
				break
		if found == True:
			bot.send_message(message.chat.id, 'Админ уже добавлен')
		else:
			add_admins_kategory(str(adding_admin)+'|'+str(adding_name)+'|'+str(message.text))		
			bot.send_message(message.chat.id, 'Админ успешно добавлен')
		adminin_admins(message)








@bot.message_handler(content_types=['text'])
def process_add_worker(message):
	if message.text == '⬅️Назад':
		adminin_workers(message)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		adding_worker = str(message.text)
		send_add_worker2 = bot.send_message(message.chat.id, 'Теперь введите его имя', reply_markup=markup)
		bot.register_next_step_handler(send_add_worker2, process_add_worker2, adding_worker)

@bot.message_handler(content_types=['text'])
def process_add_worker2(message, adding_worker):
	if message.text == '⬅️Назад':
		adminin_workers(message)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		adding_name = str(message.text)
		send_add_worker3 = bot.send_message(message.chat.id, 'Введите его @юзернейм', reply_markup=markup)
		bot.register_next_step_handler(send_add_worker3, process_add_worker3, adding_worker, adding_name)


@bot.message_handler(content_types=['text'])
def process_add_worker3(message, adding_worker, adding_name):
	if message.text == '⬅️Назад':
		adminin_workers(message)
	else:
		text = str(adding_worker)+'|'+str(message.text)

		found = False
		for i in workers_kategory:
			if str(adding_worker) in i:
				found = True
				break
		if found == True:
			bot.send_message(message.chat.id, 'Сотрудник уже добавлен')
		else:
			add_workers_kategory(str(adding_worker)+'|'+str(adding_name)+'|'+str(message.text))		
			bot.send_message(message.chat.id, 'Сотрудник успешно добавлен')
		adminin_workers(message)



















@bot.message_handler(content_types=['text'])
def workerin(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	item1 = types.KeyboardButton('Отправить кассу')
	item2 = types.KeyboardButton('')
	item3 = types.KeyboardButton('')
	item4 = types.KeyboardButton('Мой график')

	markup.add(item1, item2, item3, item4)
	bot.send_message(message.chat.id, 'Добро пожаловать, Сотрудник', reply_markup=markup)









@bot.message_handler(content_types=['text'])
def moj_grafik(message, admorwork):
    user_id = message.chat.id
    found = False
    for i in grafiky_kategory:
        if str(user_id) in i:
            found = True
    if found:
        # Если есть, отправляем кнопки "Изменить график" и "Показать график"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Изменить мой график')
        item2 = types.KeyboardButton('Показать мой график')
        item3 = types.KeyboardButton('')
        if admorwork:
        	item4 = types.KeyboardButton('⬅️Назад')
        else:
        	item4 = types.KeyboardButton('⬅️Назад к графикам')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)
    else:
        # Если нет, отправляем только кнопку "Создать график"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Создать мой график')
        item2 = types.KeyboardButton('')
        item3 = types.KeyboardButton('')
        if admorwork:
        	item4 = types.KeyboardButton('⬅️Назад')
        else:
        	item4 = types.KeyboardButton('⬅️Назад к графикам')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)
# Обработчик команды /start
@bot.message_handler(content_types=['text'])
def create_grafik_start(message):
    global selected_numbers
    selected_numbers = {}
    # Создаем клавиатуру с кнопками дней недели
    markup = create_day_buttons(selected_numbers)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Начнём создавать ваш график\n\nВыберите день недели:", reply_markup=markup)

# Обработчик команды /start
@bot.message_handler(content_types=['text'])
def show_grafik_start(message, admorwork):
    for i in grafiky_kategory:
        if str(message.chat.id) in i:
            parts = i.split("|")
            bot.send_message(message.chat.id, 'Вот ваш график\n\n'+str(parts[1])+'\n'+str(parts[2])+'\n'+str(parts[3])+'\n'+str(parts[4])+'\n'+str(parts[5])+'\n'+str(parts[6])+'\n'+str(parts[7]))

def up_grafik_start(message):
	global selected_numbers
	user_id = str(message.chat.id)
	user_grafik = None
	# Поиск нужной строки в grafiky_kategory
	for grafik in grafiky_kategory:
		if user_id in grafik:
			user_grafik = grafik
			break

	if user_grafik:
		parts = user_grafik.split("|")
		selected_numbers = {}


		for part in parts[1:]:
			day, numbers = part.split(":")
			if numbers.strip() != 'x':
				selected_numbers[day.strip()] = [num.strip() for num in numbers.split(",")]

		# Далее используйте selected_numbers для создания клавиатуры с кнопками смен
		markup = create_day_buttons(selected_numbers)
		bot.send_message(message.chat.id, "Выберите день недели для изменения:", reply_markup=markup)
	else:
		bot.send_message(message.chat.id, "Вы еще не создали график. Создайте его с помощью команды /start")
	



























@bot.message_handler(content_types=['text'])
def addkasa(message, admorwork):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('⬅️Назад')
	markup.add(item1)
	send_add_kasa = bot.send_message(message.chat.id, 'Введите кассу сегодняшней смены:\nБЕЗ валютных знаков', reply_markup=markup)
	bot.register_next_step_handler(send_add_kasa, process_add_kasa, admorwork)

@bot.message_handler(content_types=['text'])
def process_add_kasa(message, admorwork):
	if message.text == '⬅️Назад':
		if admorwork:
			workerin(message)
		else:
			adminin_kasy(message)
		
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		adding_kasa = message.text.replace(',', '.')

		if re.match(r'^[+-]?\d*\.?\d+$', adding_kasa.replace(',', '.')):
		    adding_kasa = adding_kasa.replace(',', '.')  # Заменяем запятую на точку
		    send_add_kasa2 = bot.send_message(message.chat.id, 'Введите номер вашей смены:', reply_markup=markup)
		    bot.register_next_step_handler(send_add_kasa2, process_add_kasa2, adding_kasa, admorwork)

		else:
			bot.send_message(message.chat.id, 'Вы написали не число, попробуйте снова')
			addkasa(message, admorwork)

@bot.message_handler(content_types=['text'])
def process_add_kasa2(message, adding_kasa, admorwork):
	if message.text == '⬅️Назад':
		if admorwork:
			workerin(message)
		else:
			adminin_kasy(message)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		adding_smena = message.text.replace(',', '.')

		if re.match(r'^[+-]?\d*\.?\d+$', adding_smena.replace(',', '.')):
		    adding_smena = adding_smena.replace(',', '.')  # Заменяем запятую на точку
		    send_add_kasa3 = bot.send_message(message.chat.id, 'Теперь точку на которой вы стояли', reply_markup=markup)
		    bot.register_next_step_handler(send_add_kasa3, process_add_kasa3, adding_kasa, adding_smena, admorwork)
		else:
			bot.send_message(message.chat.id, 'Вы написали не число, попробуйте снова')
			addkasa(message, admorwork)		

@bot.message_handler(content_types=['text'])
def process_add_kasa3(message, adding_kasa, adding_smena, admorwork):
	markup_kup_main = types.InlineKeyboardMarkup(row_width=1)

	item_katalog1 = types.InlineKeyboardButton('Да✅', callback_data='Y'+'|'+str(adding_kasa)+'|'+str(adding_smena)+'|'+str(message.text)+'|'+str(message.chat.id))
	item_katalog2 = types.InlineKeyboardButton('Нет❌', callback_data='N'+'|'+str(message.chat.id))

	markup_kup_main.add(item_katalog1, item_katalog2)
	
	today = datetime.date.today().strftime("%d.%m")
	current_time = datetime.datetime.now().time().strftime("%H:%M")
	print(today)
	print(current_time)
	if message.text == '⬅️Назад':
		if admorwork:
			workerin(message)
		else:
			adminin_kasy(message)
	else:
		text = str(today)+'|'+str(adding_kasa)+'|'+str(adding_smena)+'|'+str(message.text)
		bot.send_message(message.chat.id, str(today)+'✅\n'+'Зміна '+str(adding_smena)+'\n#Касса '+str(adding_kasa)+'€\n'+str(message.text)+'\n\n'+'Всё верно?', reply_markup=markup_kup_main)








@bot.message_handler(content_types=['text'])
def del_kasa_tg(message):
	found = False
	for i in admins_kategory:
		if str(message.chat.id) in i:
			found = True
			break
	if found == True:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		send_del_kasa = bot.send_message(message.chat.id, 'Введите дату кассы которую нужно удалить', reply_markup=markup)
		bot.register_next_step_handler(send_del_kasa, process_del_kasa)	
	else:
		pass

@bot.message_handler(content_types=['text'])
def process_del_kasa(message):
	if message.text == '⬅️Назад':
		adminin_kasy(message)
		
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)

		markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
		found = False
		for i in kasy_kategory:
			if str(message.text) in i:
				parts = i.split("|")
				#new_string = "|".join(parts[1:])
				new_string = str(parts[1])+' '+str(parts[3]+' '+str(parts[4])+'€ Смена '+str(parts[5])+' '+str(parts[6]))
				

				item_katalog = types.InlineKeyboardButton(new_string, callback_data='DELK|'+str(parts[0])+'|'+str(parts[4])+'|'+str(parts[3]))
				markup_kup_main.add(item_katalog)
				print(i)
				found = True
		try:
			bot.send_message(message.chat.id, 'Выбирите кассу для Удаления\n'+str(parts[2])+'✅', reply_markup=markup_kup_main)
		except:
			bot.send_message(message.chat.id, 'Такой даты нашей базе, попробуйте ещё раз', reply_markup=markup_kup_main)
			del_kasa_tg(message)












@bot.message_handler(content_types=['text'])
def up_kasa_tg(message):
	found = False
	for i in admins_kategory:
		if str(message.chat.id) in i:
			found = True
			break
	if found == True:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		send_up_kasa = bot.send_message(message.chat.id, 'Введите дату кассы которую нужно изменить', reply_markup=markup)
		bot.register_next_step_handler(send_up_kasa, process_up_kasa)
			
	else:
		pass



@bot.message_handler(content_types=['text'])
def process_up_kasa(message):
	if message.text == '⬅️Назад':
		adminin_kasy(message)
		
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)

		markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
		found = False
		for i in kasy_kategory:
			if str(message.text) in i:
				parts = i.split("|")
				#new_string = "|".join(parts[1:])
				new_string = str(parts[1])+' '+str(parts[3]+' '+str(parts[4])+'€ Смена '+str(parts[5])+' '+str(parts[6]))
				

				item_katalog = types.InlineKeyboardButton(new_string, callback_data='UPK|'+str(parts[0])+'|'+str(parts[4])+'|'+str(parts[3]))
				markup_kup_main.add(item_katalog)
				print(i)
				found = True
		try:
			bot.send_message(message.chat.id, 'Выбирите кассу для именения\n'+str(parts[2])+'✅', reply_markup=markup_kup_main)
		except:
			bot.send_message(message.chat.id, 'Такой даты нашей базе, попробуйте ещё раз', reply_markup=markup_kup_main)
			up_kasa_tg(message)
		
'''
		adding_kasa = message.text.replace(',', '.')

		if re.match(r'^[+-]?\d*\.?\d+$', adding_kasa.replace(',', '.')):
		    adding_kasa = adding_kasa.replace(',', '.')  # Заменяем запятую на точку
		    send_add_kasa2 = bot.send_message(message.chat.id, 'Введите номер вашей смены:', reply_markup=markup)
		    bot.register_next_step_handler(send_add_kasa2, process_add_kasa2, adding_kasa, admorwork)

		else:
			bot.send_message(message.chat.id, 'Вы написали не число, попробуйте снова')
			addkasa(message, admorwork)'''
@bot.message_handler(content_types=['text'])
def process_up_kasa2(message, uid, kasa):
	if message.text == '⬅️Назад':
		up_kasa_tg(message)
		
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)


		new_kasa = message.text

		send_up_kasa3 = bot.send_message(message.chat.id, 'Введите новый/старый номер смены:', reply_markup=markup)
		bot.register_next_step_handler(send_up_kasa3, process_up_kasa3, uid, kasa, new_kasa)


@bot.message_handler(content_types=['text'])
def process_up_kasa3(message, uid, kasa, new_kasa):
	if message.text == '⬅️Назад':
		up_kasa_tg(message)
		
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)

		new_smena = message.text

		send_up_kasa4 = bot.send_message(message.chat.id, 'Введите новую/старую локацию:', reply_markup=markup)
		bot.register_next_step_handler(send_up_kasa4, process_up_kasa4, uid, kasa, new_kasa, new_smena)


@bot.message_handler(content_types=['text'])
def process_up_kasa4(message, uid, kasa, new_kasa, new_smena):
	new_bod = message.text


	for i in kasy_kategory:
		partss = i.split("|")
		if str(uid) in i and str(kasa) == partss[4]:
				

			worker_name = partss[1]
			today = partss[2]
			current_time = partss[3]
			kasa1 = partss[4]
			smena = partss[5]
			bod = partss[6]



	markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
	item_katalog1 = types.InlineKeyboardButton('Да✅', callback_data='1YUPK'+'|'+str(uid)+'|'+str(kasa)+'|'+str(new_kasa)+'|'+str(new_smena)+'|'+str(new_bod)+'|'+str(current_time))
	item_katalog2 = types.InlineKeyboardButton('Нет❌', callback_data='1NUPK|'+str(today))

	markup_kup_main.add(item_katalog1, item_katalog2)
	bot.send_message(message.chat.id, 'Изменить кассу\n\n\n'+'СЕЙЧАС:\n\n'+str(worker_name)+'\n'+str(today)+'✅\n'+'Зміна '+str(smena)+'\n#Касса '+str(kasa)+'€\n'+str(bod)+'\n\n\nПОСЛЕ ИЗМЕНЕНИЙ:\n\n'+str(worker_name)+'\n'+str(today)+'✅\n'+'Зміна '+str(new_smena)+'\n#Касса '+str(new_kasa)+'€\n'+str(new_bod), reply_markup=markup_kup_main)











@bot.message_handler(content_types=['text'])
def show_workers_tg(message):
	found = False
	for i in admins_kategory:
		if str(message.chat.id) in i:
			found = True
			break
	if found == True:
		markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
		for i in workers_kategory:
			parts = i.split("|")
			item_katalog = types.InlineKeyboardButton(parts[1], callback_data='SHOWW|'+str(parts[0])+'|'+str(parts[1])+'|'+str(parts[2]))
			markup_kup_main.add(item_katalog)
		item_katalog = types.InlineKeyboardButton('⬅️Назад', callback_data='ESHOWW')
		markup_kup_main.add(item_katalog)
		bot.send_message(message.chat.id, 'Вот список сотрудников\nНажми на того кому хотите написать', reply_markup=markup_kup_main)
	else:
		pass

@bot.message_handler(content_types=['text'])
def show_admins_tg(message):
	found = False
	for i in megaadmins:
		if str(message.chat.id) in str(i):
			found = True
			break
	if found == True:
		markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
		for i in admins_kategory:
			parts = i.split("|")
			item_katalog = types.InlineKeyboardButton(parts[1], callback_data='SHOWA|'+str(parts[0])+'|'+str(parts[1])+'|'+str(parts[2]))
			markup_kup_main.add(item_katalog)
		item_katalog = types.InlineKeyboardButton('⬅️Назад', callback_data='ESHOWA')
		markup_kup_main.add(item_katalog)
		bot.send_message(message.chat.id, 'Вот список админов\nНажми на того кому хотите написать', reply_markup=markup_kup_main)
	else:
		pass







@bot.message_handler(content_types=['text'])
def show_kasy_tg(message):
	found = False
	for i in admins_kategory:
		if str(message.chat.id) in i:
			found = True
			break
	if found == True:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад')
		markup.add(item1)
		send_show_kasa = bot.send_message(message.chat.id, 'Введите дату кассы которую хотите увидеть', reply_markup=markup)
		bot.register_next_step_handler(send_show_kasa, process_show_kasa)
			
	else:
		pass

@bot.message_handler(content_types=['text'])
def process_show_kasa(message):
	if message.text == '⬅️Назад':
		adminin_kasy(message)
		
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton('⬅️Назад к касам')
		markup.add(item1)

		result = 0
		for i in kasy_kategory:
			if str(message.text) in i:
				parts = i.split("|")
				bot.send_message(message.chat.id, str(parts[1])+'\n\n'+str(parts[2])+'✅\n'+'Зміна '+str(parts[5])+'\n#Касса '+str(parts[4])+'€\n'+str(parts[6]))
				result=result+int(parts[4])
		try:
			bot.send_message(message.chat.id, 'Вот кассы за дату '+str(parts[2])+'✅\n'+'Итог: '+str(result)+'€')
			adminin_kasy(message)
		except:
			bot.send_message(message.chat.id, 'Такой даты нашей базе, попробуйте ещё раз')
			show_kasy_tg(message)







@bot.message_handler(content_types=['text'])
def show_grafiky_tg(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('⬅️Назад к графикам')
	markup.add(item1)

	for grafik in grafiky_kategory:
		partss = grafik.split("|")
		print(partss[0])
			
		found = False
		for i in admins_kategory:
			if str(partss[0]) in i:
				print(1)
				found = True
				break
		if found == True:
			parts = i.split("|")

			namet = parts[1]
			unamet = parts[2]
			bot.send_message(message.chat.id, namet+'\n'+unamet+'\n\n'+partss[1]+'\n'+partss[2]+'\n'+partss[3]+'\n'+partss[4]+'\n'+partss[5]+'\n'+partss[6]+'\n'+partss[7], reply_markup=markup)
		else:
			found2 = False
			for i2 in workers_kategory:
				if str(partss[0]) in str(i2):
					found2 = True
					break
			if found2 == True:
				parts = i2.split("|")

				namet = parts[1]
				unamet = parts[2]
				bot.send_message(message.chat.id, namet+'\n'+unamet+'\n\n'+partss[1]+'\n'+partss[2]+'\n'+partss[3]+'\n'+partss[4]+'\n'+partss[5]+'\n'+partss[6]+'\n'+partss[7], reply_markup=markup)
			else:
				pass
	else:
		pass





@bot.message_handler(content_types=['text'])
def do_tomorrow_grakify(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('⬅️Назад к графикам')
	markup.add(item1)

	current_date = datetime.date.today()
	today = datetime.date.today().strftime("%d.%m")
	# Получаем завтрашнюю дату
	tomorrow_date = current_date + datetime.timedelta(days=1)
	# Получаем день недели для завтрашней даты (0 - понедельник, 1 - вторник, и т.д.)
	day_of_week = tomorrow_date.weekday()
	# Список названий дней недели
	days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
	# Название завтрашнего дня недели
	tomorrow_day_of_week = days_of_week[day_of_week]
	print(tomorrow_day_of_week)


	resultfor1 = []
	resultfor2 = []
	resultfor3 = []
	resultfor4 = []

	for grafik in grafiky_kategory:
		partss = grafik.split("|")
		print(partss[0])
			
		found = False
		for i in admins_kategory:
			if str(partss[0]) in i:
				print(1)
				found = True
				break
		if found == True:
			parts = i.split("|")

			namet = parts[1]
			unamet = parts[2]
			for i in partss:
				if str(tomorrow_day_of_week) in i:
					if str('1') in i:
						resultfor1.append(namet)
					if str('2') in i:
						resultfor2.append(namet)
					if str('3') in i:
						resultfor3.append(namet)
					if str('4') in i:
						resultfor4.append(namet)

						
			
		else:
			found2 = False
			for i2 in workers_kategory:
				if str(partss[0]) in str(i2):
					found2 = True
					break
			if found2 == True:
				parts = i2.split("|")

				namet = parts[1]
				unamet = parts[2]
				for i in partss:
					if str(tomorrow_day_of_week) in i:
						if str('1') in i:
							resultfor1.append(namet)
						if str('2') in i:
							resultfor2.append(namet)
						if str('3') in i:
							resultfor3.append(namet)
						if str('4') in i:
							resultfor4.append(namet)
				
			else:
				pass



	result = '1 смена - '+', '.join(resultfor1) + '\n2 смена - ' + ', '.join(resultfor2) + '\n3 смена - ' + ', '.join(resultfor3) + '\n4 смена - ' + ', '.join(resultfor4)
	bot.send_message(message.chat.id, 'Вот список сотрудников которые могут встать на смены\n\n'+'График на '+str(today)+'✅('+str(tomorrow_day_of_week)+')\n\n'+str(result), reply_markup=markup)









@bot.callback_query_handler(func=lambda call:True)
def kategory_asort(call):
	global selected_numbers
	user_id = str(call.message.chat.id)
	user_grafik = None

	for grafik in grafiky_kategory:
	    if user_id in grafik:
	        user_grafik = grafik
	        break

	if call.data == 'done':
	    if selected_numbers:
	        day_selections = []
	        for day in ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']:
	            numbers = selected_numbers.get(day, [])
	            if numbers:
	                numbers.sort()
	                day_selections.append(f"{day}: {', '.join(numbers)}")
	            else:
	                day_selections.append(f"{day}: x")

	        selections = "\n".join(day_selections)
	        selections2 = "|".join(day_selections)

	        if user_grafik:
	        	update_grafiky_kategory(user_grafik, f"{user_id}|{selections2}")
	        	selected_numbers = {}  # Обнуляем selected_numbers
	        	bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
	        	bot.send_message(call.message.chat.id, f"Вы изменили график\n{selections}")
	        else:
	        	add_grafiky_kategory(f"{user_id}|{selections2}")
	        	print(selected_numbers)
	        	selected_numbers = {}  # Обнуляем selected_numbers
	        	bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
	        	bot.send_message(call.message.chat.id, f"Вы создали вот такой график\n{selections}")

	        found = False
	        admorwork = False
	        for i in workers_kategory:
	            if str(call.message.chat.id) in i:
	                found = True
	                break
	        if found:
	            admorwork = True
	            moj_grafik(call.message, admorwork)
	        else:
	            found = False
	            for i in admins_kategory:
	                if str(call.message.chat.id) in i:
	                    found = True
	                    break
	            if found:
	                admorwork = False
	                moj_grafik(call.message, admorwork)

	    else:
	        bot.send_message(call.message.chat.id, "Попробуйте ещё раз")

	elif call.data.startswith('day_'):
	    # Обработка нажатия на кнопку с днем недели
	    day = call.data.split('_')[1]
	    markup = create_number_buttons(day)
	    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
	                                  reply_markup=markup)
	elif call.data == 'back':
	    # Обработка нажатия на кнопку "Назад"
	    markup = create_day_buttons(selected_numbers)
	    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
	                                  reply_markup=markup)
	elif call.data == 'back2':
	    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
	    found = False
	    admorwork = False
	    for i in workers_kategory:
	        if str(call.message.chat.id) in i:
	            found = True
	            break
	    if found:
	        admorwork = True
	        moj_grafik(call.message, admorwork)
	    else:
	        found = False
	        for i in admins_kategory:
	            if str(call.message.chat.id) in i:
	                found = True
	                break
	        if found:
	            admorwork = False
	            moj_grafik(call.message, admorwork)
	        else:
	            pass
	elif call.data.startswith('number_'):
	    # Обработка нажатия на кнопку с числом
	    day, number = call.data.split('_')[1:]
	    if day not in selected_numbers:
	        selected_numbers[day] = []
	    if number in selected_numbers[day]:
	        selected_numbers[day].remove(number)
	    else:
	        selected_numbers[day].append(number)
	    markup = create_number_buttons(day)
	    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
	                                  reply_markup=markup)














	if call.message:
		if call.data.startswith('Y'):
			today = datetime.date.today().strftime("%d.%m")
			current_time = datetime.datetime.now().time().strftime("%H:%M")
			

			parts = call.data.split("|")
			status = parts[0]
			kasa = parts[1]
			smena = parts[2]
			bod = parts[3]
			uid = parts[4]


			found = False
			for i in workers_kategory:
				if str(uid) in i:
					partss = i.split("|")
					worker_name = partss[1]
					found = True
					break
			if found == True:
				add_kasy_kategory(str(uid)+'|'+str(worker_name)+'|'+str(today)+'|'+str(current_time)+'|'+str(kasa)+'|'+str(smena)+'|'+str(bod))
				bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
				bot.send_message(uid, 'Касса успешно добавлена')
				workerin(call.message)
			else:	
				found = False
				for i in admins_kategory:
					if str(uid) in i:
						partss = i.split("|")
						worker_name = partss[1]
						found = True
						break
				if found == True:
					add_kasy_kategory(str(uid)+'|'+str(worker_name)+'|'+str(today)+'|'+str(current_time)+'|'+str(kasa)+'|'+str(smena)+'|'+str(bod))
					bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
					bot.send_message(uid, 'Касса успешно добавлена')
					adminin_kasy(call.message)
				else:
					pass


			
			for i in workers_kategory:
				partsss = i.split("|")
				idinbd = partsss[0]

				bot.send_message(idinbd, str(worker_name)+'\n\n'+str(today)+'✅\n'+'Зміна '+str(smena)+'\n#Касса '+str(kasa)+'€\n'+str(bod))
			for i in admins_kategory:
				partsss = i.split("|")
				idinbd = partsss[0]

				bot.send_message(idinbd, str(worker_name)+'\n\n'+str(today)+'✅\n'+'Зміна '+str(smena)+'\n#Касса '+str(kasa)+'€\n'+str(bod))
			




		if call.data.startswith('N'):
			partss = call.data.split("|")
			uid = partss[1]
			found = False
			admorwork = False
			for i in workers_kategory:
				if str(uid) in i:
					found = True
					break
			if found == True:
				admorwork = True
				bot.send_message(uid, 'Хорошо, попробуйте заново')
				addkasa(call.message, admorwork)
			else:	
				found = False
				for i in admins_kategory:
					if str(uid) in i:
						found = True
						break
				if found == True:
					admorwork = False
					bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
					bot.send_message(uid, 'Хорошо, попробуйте заново')
					addkasa(call.message, admorwork)
				else:
					pass







		



		if call.data.startswith('DELW'):
			parts = call.data.split("|")

			new_text = "|".join(parts[1:])

			markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
			
			item_katalog1 = types.InlineKeyboardButton('Да✅', callback_data='1YDELW|'+str(new_text))
			item_katalog2 = types.InlineKeyboardButton('Нет❌', callback_data='1NDELW')
			markup_kup_main.add(item_katalog1, item_katalog2)

			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы хотите удалить сотрудника:\n\n"+str(parts[2]), reply_markup=markup_kup_main)


		if call.data.startswith('1YDELW'):

			parts = call.data.split("|")

			new_text = "|".join(parts[1:])

			remove_workers_kategory(new_text)
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.send_message(call.message.chat.id, 'Сотрудник '+str(parts[2])+' успешно удалён')
			adminin_workers(call.message)
			try:
				bot.send_message(parts[1], 'Вы больше не можете пользиваться ботом')
			except:
				pass
		if call.data == '1NDELW':
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			adminin_workers(call.message)







		if call.data.startswith('DELA'):
			parts = call.data.split("|")

			new_text = "|".join(parts[1:])

			markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
			
			item_katalog1 = types.InlineKeyboardButton('Да✅', callback_data='1YDELA|'+str(new_text))
			item_katalog2 = types.InlineKeyboardButton('Нет❌', callback_data='1NDELA')
			markup_kup_main.add(item_katalog1, item_katalog2)

			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вы хотите удалить админа:\n\n"+str(parts[2]), reply_markup=markup_kup_main)


		if call.data.startswith('1YDELA'):

			parts = call.data.split("|")

			new_text = "|".join(parts[1:])

			remove_admins_kategory(new_text)
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.send_message(call.message.chat.id, 'Админ '+str(parts[2])+' успешно удалён')
			adminin(call.message)
			try:
				bot.send_message(parts[1], 'Вы больше не можете пользиваться ботом')
			except:
				pass
		if call.data == '1NDELA':
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			adminin(call.message)
















		if call.data.startswith('UPK'):
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1 = types.KeyboardButton('⬅️Назад')
			markup.add(item1)
			parts = call.data.split("|")
			uid = parts[1]
			kasa = parts[2]
			time = parts[3]
			for i in kasy_kategory:
				partss = i.split("|")
				if str(uid) in i and str(kasa) == partss[4] and str(time) == partss[3]:
					

					worker_name = partss[1]
					today = partss[2]
					current_time = [3]
					kasa1 = partss[4]
					smena = partss[5]
					bod = partss[6]

					bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
					bot.send_message(call.message.chat.id, str(worker_name)+'\n\n'+str(today)+'✅\n'+'Зміна '+str(smena)+'\n#Касса '+str(kasa1)+'€\n'+str(bod))
					send_up_kasa2 = bot.send_message(call.message.chat.id, 'Ввведите новую/старую кассу', reply_markup=markup)
					bot.register_next_step_handler(send_up_kasa2, process_up_kasa2, uid, kasa)


		if call.data.startswith('1YUPK'):
			
			parts = call.data.split("|")

			uid = parts[1]
			kasa = parts[2]
			
			new_kasa = parts[3]
			new_smena = parts[4]
			new_bod = parts[5]
			current_time = parts[6]
			


			for i in kasy_kategory:
				
				partss = i.split("|")
				if str(uid) in i and str(kasa) == partss[4] and str(current_time) == partss[3]:
					
					

					worker_name = partss[1]
					today = partss[2]
					current_time = partss[3]
					kasa1 = partss[4]
					smena = partss[5]
					bod = partss[6]

					update_kasy_kategory(str(uid)+'|'+str(worker_name)+'|'+str(today)+'|'+str(current_time)+'|'+str(kasa)+'|'+str(smena)+'|'+str(bod), str(uid)+'|'+str(worker_name)+'|'+str(today)+'|'+str(current_time)+'|'+str(new_kasa)+'|'+str(new_smena)+'|'+str(new_bod))
					#bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
					bot.send_message(call.message.chat.id, 'Каса успешнои Изменена')
					bot.send_message(call.message.chat.id, str(worker_name)+'\n'+str(today)+'✅\n'+'Зміна '+str(new_smena)+'\n#Касса '+str(new_kasa)+'€\n'+str(new_bod))
					adminin_kasy(call.message)


		if call.data.startswith('1NUPK'):
			parts = call.data.split("|")
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.send_message(call.message.chat.id, 'Попробуйте снова')
			up_kasa_tg(call.message)













		if call.data.startswith('SHOWW'):
			parts = call.data.split("|")
			markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
			item_katalog = types.InlineKeyboardButton('⬅️Назад', callback_data='E2SHOWW|'+str(parts[0])+'|'+str(parts[1])+'|'+str(parts[2]))
			markup_kup_main.add(item_katalog)
			
			uid = parts[1]
			name = parts[2]
			usn = parts[3]
			for i in workers_kategory:
				partss = i.split("|")
				if str(uid) in i and str(name) == partss[1]:
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вот аккаунт сотрудника "+str(name)+'\n\n'+str(usn), reply_markup=markup_kup_main)

		if call.data.startswith('E2SHOWW'):
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			show_workers_tg(call.message)


		if call.data.startswith('ESHOWW'):
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			adminin_workers(call.message)



		if call.data.startswith('SHOWA'):
			parts = call.data.split("|")
			markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
			item_katalog = types.InlineKeyboardButton('⬅️Назад', callback_data='E2SHOWA|'+str(parts[0])+'|'+str(parts[1])+'|'+str(parts[2]))
			markup_kup_main.add(item_katalog)
			
			uid = parts[1]
			name = parts[2]
			usn = parts[3]
			for i in admins_kategory:
				partss = i.split("|")
				if str(uid) in i and str(name) == partss[1]:
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вот аккаунт админа "+str(name)+'\n\n'+str(usn), reply_markup=markup_kup_main)

		if call.data.startswith('E2SHOWA'):
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			show_admins_tg(call.message)


		if call.data.startswith('ESHOWA'):
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			adminin(call.message)










		if call.data.startswith('DELK'):
			markup_kup_main = types.InlineKeyboardMarkup(row_width=1)
			
			parts = call.data.split("|")
			uid = parts[1]
			kasa = parts[2]
			time = parts[3]
			for i in kasy_kategory:
				partss = i.split("|")
				if str(uid) in i and str(kasa) == partss[4] and str(time) == partss[3]:
					item_katalog1 = types.InlineKeyboardButton('Да✅', callback_data='1YDELK'+'|'+str(uid)+'|'+str(kasa)+'|'+str(time))
					item_katalog2 = types.InlineKeyboardButton('Нет❌', callback_data='1NDELK')

					markup_kup_main.add(item_katalog1, item_katalog2)
					

					worker_name = partss[1]
					today = partss[2]
					current_time = [3]
					kasa1 = partss[4]
					smena = partss[5]
					bod = partss[6]

					bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
					bot.send_message(call.message.chat.id, 'Вы хотите удалить кассу:\n\n'+str(worker_name)+'\n\n'+str(today)+'✅\n'+'Зміна '+str(smena)+'\n#Касса '+str(kasa1)+'€\n'+str(bod), reply_markup=markup_kup_main)
					
		if call.data.startswith('1YDELK'):
			parts = call.data.split("|")

			uid = parts[1]
			kasa = parts[2]
			time = parts[3]
			


			for i in kasy_kategory:
				partss = i.split("|")
				if str(uid) in i and str(kasa) == partss[4] and str(time) == partss[3]:
					

					worker_name = partss[1]
					today = partss[2]
					current_time = partss[3]
					kasa1 = partss[4]
					smena = partss[5]
					bod = partss[6]

					remove_kasy_kategory(str(uid)+'|'+str(worker_name)+'|'+str(today)+'|'+str(current_time)+'|'+str(kasa)+'|'+str(smena)+'|'+str(bod))
					#bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
					bot.send_message(call.message.chat.id, 'Каса успешнои Удалена')
					adminin_kasy(call.message)


		if call.data.startswith('1NDELK'):
			parts = call.data.split("|")
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.send_message(call.message.chat.id, 'Попробуйте снова')
			del_kasa_tg(call.message)

			

				






def create_day_buttons(selected_numbers):
    markup = types.InlineKeyboardMarkup()
    days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    for day in days_of_week:
        shifts = selected_numbers.get(day, [])
        shift_text = sorted(filter(lambda x: x != 'x', shifts), key=int)
        shift_text_str = ", ".join(shift_text) if shift_text else "x"
        markup.add(types.InlineKeyboardButton(text=f"{day}: {shift_text_str}", callback_data=f'day_{day}'))
    markup.add(types.InlineKeyboardButton(text='Готово✅', callback_data='done'))
    markup.add(types.InlineKeyboardButton(text='⬅️Назад', callback_data='back2'))
    return markup





# Функция для создания клавиатуры с кнопками чисел для выбранного дня
def create_number_buttons(day):
    markup = types.InlineKeyboardMarkup()
    numbers = ['1', '2', '3', '4']
    for number in numbers:
        text = f'✅ {number}' if number in selected_numbers.get(day, []) else number
        markup.add(types.InlineKeyboardButton(text=text, callback_data=f'number_{day}_{number}'))
    markup.add(types.InlineKeyboardButton(text='⬅️Назад', callback_data='back'))
    return markup


bot.polling()