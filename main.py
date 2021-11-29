import telebot, config, stock
bot = telebot.TeleBot(config.TOKEN)
menu_start = telebot.types.ReplyKeyboardMarkup(True)
menu_selling_stock = telebot.types.ReplyKeyboardMarkup(True)
menu_buying_stock = telebot.types.ReplyKeyboardMarkup(True)
empty = telebot.types.ReplyKeyboardMarkup(False)

def make_menu():
    menu_start.row("Купить акцию", "Продать акцию")
    menu_start.row("Портфель акций")
    menu_buying_stock.row("Home")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'У тебя есть 1000$. Попробуй себя в инвестициях. На 1000000$ будет пасхалка', reply_markup=menu_start)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Sort it out yourself")

@bot.message_handler(content_types=['text'])
def send_feedback(message):
    if (message.text == "Купить акцию"):
        bot.send_message(message.chat.id, "Введите название акции", reply_markup=menu_buying_stock)
        bot.register_next_step_handler(message, buy_stock)
    if message.text == "Home":
        bot.send_message(message.chat.id, "Главная страница", reply_markup=menu_start)

def buy_stock(message):
    bot.send_message(message.chat.id, "Wait")
    try:
        ans = "Price: " + str(stock.get_info(message.text).info["currentPrice"]) + " " + stock.get_info(message.text).info["financialCurrency"]
        ans += '\n' + "recommendation: " + stock.get_info(message.text).info['recommendationKey']
        bot.send_message(message.chat.id, ans)
    except:
        bot.send_message(message.chat.id, "Не нашел")
    bot.register_next_step_handler(message, buy_stock)
make_menu()
bot.polling()