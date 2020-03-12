import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/enterSticker.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Св. аудит. 1k 🎯")
	item2 = types.KeyboardButton("Св. аудит. 2k 🎯")
	item3 = types.KeyboardButton("Св. аудит. 3k 🎯")
	item4 = types.KeyboardButton("Св. аудит. 4k 🎯")
	item5 = types.KeyboardButton("Св. аудит. 5k 🎯")
	markup.add(item1,item2,item3,item4,item5)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот чтобы помочь вам найти свободную аудиторию на территории БГУИРа.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Св. аудит. 1k 🎯':
            auditories = config.search_empty_auditory()
            i = 1
            for j in auditories[str(1)]:
                if auditories[str(1)][j] == 0 and i < 11:
                    bot.send_message(message.chat.id, str(j))
                i += 1
        if message.text == 'Св. аудит. 2k 🎯':
            auditories = config.search_empty_auditory()
            i = 1
            for j in auditories[str(2)]:
                if auditories[str(2)][j] == 0 and i < 11:
                    bot.send_message(message.chat.id, str(j))
                i += 1
        if message.text == 'Св. аудит. 3k 🎯':
            auditories = config.search_empty_auditory()
            i = 1
            for j in auditories[str(3)]:
                if auditories[str(3)][j] == 0 and i < 11:
                    bot.send_message(message.chat.id, str(j))
                i += 1
        if message.text == 'Св. аудит. 4k 🎯':
            auditories = config.search_empty_auditory()
            i = 1
            for j in auditories[str(4)]:
                if auditories[str(4)][j] == 0 and i < 11:
                    bot.send_message(message.chat.id, str(j))
                i += 1
        if message.text == 'Св. аудит. 5k 🎯':
            auditories = config.search_empty_auditory()
            i = 1
            for j in auditories[str(5)]:
                if auditories[str(5)][j] == 0 and i < 11:
                    bot.send_message(message.chat.id, str(j))
                i += 1
        # else:
        # 	bot.send_message(message.chat.id, 'Я не знаю что ещё написать 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Бывает 😢')

			# remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
				reply_markup=None)

			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)
# elif message.text == '😊 Как дела?':
#
# 	markup = types.InlineKeyboardMarkup(row_width=2)
# 	item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
# 	item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
#
# 	markup.add(item1, item2)
#
# 	bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
