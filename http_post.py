import telebot
import requests
import logging
from telebot import types
from Sensorlog.Post import Decode, Events, Values

# Detalhes sobre a API do telegram
# https://core.telegram.org/bots/api

# Detalhes sobre a lib telebot
# https://github.com/eternnoir/pyBotAPI

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Substitua o token pelo seu token criado com o BotFather (https://t.me/BotFather)
TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
EVENT_URL = "http://example.com/event" # Substitua pela URL desejada
VALUES_URL = "http://example.com/values" # Substitua pela URL desejada
# Adicione seu bot num canal de LOG.
# Quando um sensor fizer alguma Evento o método process_post_event será chamado
# com o evento de notificação do sensor.
# Quando uma publicação de valores de sensor for publicada,
# o método process_post_values será chamado com os valores dos sensores

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)


def send_post_request(url, json):
    """
    Envia uma solicitação POST para a URL especificada com os dados fornecidos.

    Args:
        url (str): A URL para onde a solicitação POST será enviada.
        json (str): Os dados a serem enviados na solicitação POST.

    Returns:
        requests.Response: A resposta da solicitação POST.
    """
    logger.info("Iniciando envio de solicitação POST")
    try:
        response = requests.post(url, json=json, timeout=10)
        logger.info(f"Solicitação POST enviada para {url} com dados {json}")
        return response
    except Exception as e:
        logger.error(f"Erro ao enviar solicitação POST: {e}")
    logger.info("Finalizando envio de solicitação POST")


def process_post_event(event: Events):
    """
    Processa eventos recebidos do canal do Telegram.

    Args:
        event (Events): Objeto que representa um evento de sensor.
    """
    logger.info("Iniciando processamento do evento")
    try:
        url = EVENT_URL
        logger.info(f"Enviando evento para {url}: {event}")
        response = send_post_request(url, event.to_json())
        logger.info(f"Resposta do servidor: {response.status_code}")
        print(response)
    except Exception as e:
        logger.error(f"Erro ao processar evento: {e}")
    logger.info("Finalizando processamento do evento")


def process_post_values(values: Values):
    """
    Processa valores de sensores recebidos do canal do Telegram.

    Args:
        values (Values): Objeto que representa os valores dos sensores.
    """
    logger.info("Iniciando processamento dos valores")
    try:
        url = VALUES_URL
        logger.info(f"Enviando valores para {url}: {values}")
        response = send_post_request(url, values.to_json())
        logger.info(f"Resposta do servidor: {response.status_code}")
        print(response)
    except Exception as e:
        logger.error(f"Erro ao processar valores: {e}")
    logger.info("Finalizando processamento dos valores")


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
    logger.info("Iniciando manipulação da mensagem do canal")
    try:
        message = Decode(m)
        if isinstance(message.var_data, Values):
            process_post_values(message.var_data)
        elif isinstance(message.var_data, Events):
            process_post_event(message.var_data)
    except Exception as e:
        logger.error(f"Erro ao manipular mensagem do canal: {e}")
    logger.info("Finalizando manipulação da mensagem do canal")


logger.info("Bot iniciado. Aguardando mensagens do canal")
bot.infinity_polling(skip_pending=False)
