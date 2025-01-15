import telebot
from telebot import types
from Sensorlog.Post import Decode, Events, Values, EVENT_LEVEL, EVENT_COMMUNICATION
import requests
import json

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


def send_post_request(url, data):
    """
    Envia uma solicitação POST para a URL especificada com os dados fornecidos.

    Args:
        url (str): A URL para onde a solicitação POST será enviada.
        data (dict): Os dados a serem enviados na solicitação POST.

    Returns:
        requests.Response: A resposta da solicitação POST.
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response


def process_post_event(event: Events):
    """
    Processa eventos recebidos do canal do Telegram.

    Args:
        event (Events): Objeto que representa um evento de sensor.
    """
    url = "http://example.com/event"  # Substitua pela URL desejada
    response = send_post_request(url, event.__dict__)
    print(response)


def process_post_values(values: Values):
    """
    Processa valores de sensores recebidos do canal do Telegram.

    Args:
        values (Values): Objeto que representa os valores dos sensores.
    """
    url = "http://example.com/values"  # Substitua pela URL desejada
    response = send_post_request(url, values.__dict__)
    print(response)


def filter_direct_channel_text_signed(m: types.Message) -> bool:
    """
    Filtra mensagens de texto diretas assinadas em um canal.

    Args:
        m (types.Message): A mensagem recebida do canal do Telegram.

    Returns:
        bool: True se a mensagem atender aos critérios de filtro, False caso contrário.
    """
    return (
        m.reply_to_message is None
        and m.forward_from_chat is None
        and m.author_signature is not None
        and m.content_type == "text"
        and m.chat.type == "channel"
    )


@bot.channel_post_handler(func=filter_direct_channel_text_signed)
def handle_channel_post(m: types.Message):
    """
    Manipula postagens de canal filtradas.

    Args:
        m (types.Message): A mensagem recebida do canal do Telegram.
    """
    message = Decode(m)
    if isinstance(message.var_data, Values):
        process_post_values(message.var_data)
    elif isinstance(message.var_data, Events):
        process_post_event(message.var_data)


bot.infinity_polling(skip_pending=False)
