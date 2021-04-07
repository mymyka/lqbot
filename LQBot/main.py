import cfg
import lib
import qrcode
import telebot

bot = telebot.TeleBot(cfg.TOKEN)

Queues = {
    "active": {
        "total": {},
        "ready": {},
        "clientsList": {}
    },

    "static": {
        "name": {},
        "host": {},
        "message": {},
        "maxPeople": {},
        "timeLimits": {
            "min": {},
            "max": {}
        }
    }
}

Clients = {
    "active": {
        "status": {},
        "queue": {},
        "position": {}
    },

    "static": {
        "name": {},
        "surname": {},
        "trust": {},
        "placeList": {}
    }
}


@bot.message_handler(commands=["Start"])
def start(message):
    bot.send_message(message.chat.id, cfg.Start_Message)

    msg = bot.send_message(message.chat.id, "Enter text")
    bot.register_next_step_handler(msg, process_fullname_step)


def process_fullname_step(message):
    print(message.text)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, cfg.Help_Message)


@bot.message_handler(commands=["Status-mymy"])
def status(message):
    bot.send_message(message.chat.id,
                     "Кількість активних черг: {}\nКількість користувачів: {}\n".format(len(Queues), len(Clients)))


if __name__ == '__main__':
    bot.infinity_polling()
