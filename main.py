import telebot
from telebot import types
from Sensorlog.Post import Decode
from Sensorlog.Post import Events
from Sensorlog.Post import Values
from Sensorlog.Post import EVENT_LEVEL
from Sensorlog.Post import EVENT_COMMUNICATION

# Detalhes sobre a API do telegram
# https://core.telegram.org/bots/api

# Detalhes sobre a lib telebot
# https://github.com/eternnoir/pyBotAPI

# Substitua o token pelo seu token criado com o BotFather (https://t.me/BotFather)
TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"

# Adicione seu bot num canal de LOG.
# Quando um sensor fizer alguma Evento o método process_post_event será chamado
# com o evento de notificação do sensor.
# Quando uma publicação de valores de sensor for publicada,
# o método process_post_values será chamado com os valores dos sensores


bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


def process_post_event(event: Events):
    if event.type == EVENT_LEVEL:
        print(f"Evento de nível:\n{event}")

    elif event.type == EVENT_COMMUNICATION:
        print(f"Evento de comunicação:\n{event}")

    else:
        print(f"Evento desconhecido:\n{event}")


def process_post_values(values: Values):
    print(f"Valores de sensores recebidos:\n{values}")


def filter_direct_channel_text_signed(m: types.Message) -> bool:
    return (
        m.reply_to_message is None
        and m.forward_from_chat is None
        and m.author_signature is not None
        and m.content_type == "text"
        and m.chat.type == "channel"
    )


@bot.channel_post_handler(func=filter_direct_channel_text_signed)
def handle_channel_post(m: types.Message):

    message = Decode(m)
    if isinstance(message.var_data, Values):
        process_post_values(message.var_data)
    elif isinstance(message.var_data, Events):
        process_post_event(message.var_data)


bot.infinity_polling(skip_pending=False)
