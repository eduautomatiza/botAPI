import telebot
from telebot import types
from Sensorlog.Post import Decode, Events, Values, EVENT_LEVEL, EVENT_COMMUNICATION
import sqlite3

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


def insert_into_db(table, data):
    """
    Insere dados em uma tabela do banco de dados SQLite.

    Args:
        table (str): O nome da tabela onde os dados serão inseridos.
        data (dict): Os dados a serem inseridos na tabela.

    Returns:
        None
    """
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    columns = ", ".join(data.keys())
    placeholders = ", ".join("?" * len(data))
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    cursor.execute(sql, tuple(data.values()))
    conn.commit()
    conn.close()


def process_post_event(event: Events):
    """
    Processa eventos recebidos do canal do Telegram.

    Args:
        event (Events): Objeto que representa um evento de sensor.

    A função insere os dados do evento na tabela 'events' do banco de dados.
    """
    insert_into_db("events", event.__dict__)


def process_post_values(values: Values):
    """
    Processa valores de sensores recebidos do canal do Telegram.

    Args:
        values (Values): Objeto que representa os valores dos sensores.

    A função insere os valores dos sensores na tabela 'values' do banco de dados.
    """
    insert_into_db("values", values.__dict__)


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

    A função decodifica a mensagem e processa os dados de eventos ou valores dos sensores.
    """
    message = Decode(m)
    if isinstance(message.var_data, Values):
        process_post_values(message.var_data)
    elif isinstance(message.var_data, Events):
        process_post_event(message.var_data)


bot.infinity_polling(skip_pending=False)
