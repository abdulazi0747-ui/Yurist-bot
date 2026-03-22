import telebot

# BotFather bergan tokenni shu yerga qo'ying
# DIQQAT: Tokeningizni qo'shtirnoq ichiga yozing
BOT_TOKEN = "7547007785:AAHYX5yvT85Z6I0jU2f4Z3g3g3g3g3g3g3g" 

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Yurist Yonimda AI botingiz Render-da muvaffaqiyatli ishga tushdi! ✅\n\nSavolingizni yozib qoldiring.")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, "💡 Savolingiz qabul qilindi. Tez orada tahlil qilib javob beraman.")

print("Bot ishga tushdi...")
bot.infinity_polling()
