import telebot
from telebot import types
import pickle

# Токен вашего бота
TOKEN = '6872203027:AAGWv2jLJ1EEAH_1vbDM1a6I421UiaPJ97Q'

# Создание объекта бота
bot = telebot.TeleBot(TOKEN)

# Загрузка данных из файла
try:
    with open("grafiky.pkl", "rb") as file:
        grafiky_kategory = pickle.load(file)
except FileNotFoundError:
    grafiky_kategory = []

selected_numbers = {}



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


@bot.message_handler(commands=['start'])
def start_com(message): 
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
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)
    else:
        # Если нет, отправляем только кнопку "Создать график"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Создать мой график')
        markup.add(item)
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Создать мой график':
        create_grafik_start(message)
    if message.text == 'Показать мой график':
        show_grafik_start(message)
    if message.text == 'Изменить мой график':
        up_grafik_start(message)






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
def show_grafik_start(message):
    for i in grafiky_kategory:
        if str(message.chat.id) in i:
            parts = i.split("|")
            bot.send_message(message.chat.id, 'Вот ваш график\n\n'+str(parts[1])+'\n'+str(parts[2])+'\n'+str(parts[3])+'\n'+str(parts[4])+'\n'+str(parts[5])+'\n'+str(parts[6])+'\n'+str(parts[7]))
def up_grafik_start(message):
    user_id = str(message.chat.id)
    user_grafik = None
    
    for grafik in grafiky_kategory:
        if user_id in grafik:
            user_grafik = grafik
            break
    
    if user_grafik:
        selected_numbers = {}  # Обнуляем selected_numbers
        parts = user_grafik.split("|")
        for part in parts[1:]:
            day, numbers = part.split(":")
            selected_numbers[day.strip()] = [num.strip() for num in numbers.split(",")]

        markup = create_day_buttons(selected_numbers)  # Передаем selected_numbers в функцию
        bot.send_message(message.chat.id, "Выберите день недели для изменения:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Вы еще не создали график. Создайте его с помощью команды /start")




# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
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
                for i in grafiky_kategory:
                    if str(call.message.chat.id) in i:
                        update_grafiky_kategory(i, f"{user_id}|{selections2}")
                        bot.send_message(call.message.chat.id, f"Вы изменили график\n{selections}")
            else:
                add_grafiky_kategory(f"{user_id}|{selections2}")
                bot.send_message(call.message.chat.id, f"Вы создали вот такой график\n{selections}")
            
            start_com(call.message)
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
        start_com(call.message)
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

def create_day_buttons(selected_numbers):
    markup = types.InlineKeyboardMarkup()
    days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    for day in days_of_week:
        shifts = selected_numbers.get(day, [])
        shift_text = sorted(filter(lambda x: x != 'x', shifts), key=int)
        shift_text_str = ", ".join(shift_text) if shift_text else "x"
        markup.add(types.InlineKeyboardButton(text=f"{day}: {shift_text_str}", callback_data=f'day_{day}'))
    markup.add(types.InlineKeyboardButton(text='Готово', callback_data='done'))
    markup.add(types.InlineKeyboardButton(text='Назад', callback_data='back2'))
    return markup





# Функция для создания клавиатуры с кнопками чисел для выбранного дня
def create_number_buttons(day):
    markup = types.InlineKeyboardMarkup()
    numbers = ['1', '2', '3', '4']
    for number in numbers:
        text = f'✅ {number}' if number in selected_numbers.get(day, []) else number
        markup.add(types.InlineKeyboardButton(text=text, callback_data=f'number_{day}_{number}'))
    markup.add(types.InlineKeyboardButton(text='Назад', callback_data='back'))
    return markup

# Запуск бота
bot.polling()