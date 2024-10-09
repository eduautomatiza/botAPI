import telebot
from telebot import types
from TelegramDecodePost import TelegramDecodePost
from TelegramDecodePost import TelegramEvents
from TelegramDecodePost import TelegramValues
from TelegramDecodePost import EVENT_LEVEL
from TelegramDecodePost import EVENT_COMMUNICATION

# Detalhes sobre a API do telegram
# https://core.telegram.org/bots/api

# Detalhes sobre a lib telebot
# https://github.com/eternnoir/pyTelegramBotAPI

# Substitua o token pelo seu token criado com o BotFather (https://t.me/BotFather)
TELEGRAM_TOKEN = "TOKEN"

# Adicione seu bot num canal de LOG.
# Quando um sensor fizer alguma Evento o método process_post_event será chamado
# com o evento de notificação do sensor.
# Quando uma publicação de valores de sensor for publicada,
# o método process_post_values será chamado com os valores dos sensores


bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


def process_post_event(event: TelegramEvents):
    if event.type == EVENT_LEVEL:
        print(f"Evento de nível:\n{event}")

    elif event.type == EVENT_COMMUNICATION:
        print(f"Evento de comunicação:\n{event}")

    else:
        print(f"Evento desconhecido:\n{event}")


def process_post_values(values: TelegramValues):
    print(f"Valores de sensores recebidos:\n{values}")


@bot.channel_post_handler(func=lambda m: m.author_signature is not None)
def handle_channel_post(m: types.Message):

    message = TelegramDecodePost(m)
    if message.is_forward is False:
        if isinstance(message.var_data, TelegramValues):
            process_post_values(message.var_data)
        elif isinstance(message.var_data, TelegramEvents):
            process_post_event(message.var_data)


bot.infinity_polling(skip_pending=False)
