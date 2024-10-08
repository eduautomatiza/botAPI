import re
from telebot import types
from TelegramValues import TelegramValues
from TelegramSetValues import TelegramSetValues
from TelegramEvents import TelegramEvents


SYMBOL_CHECK:str = "\u2705"  # CHECK MARK
SYMBOL_WARNING:str = "\u26A0"  # warning
SYMBOL_DOWN_ARROW:str = "\u2B07"  # down arrow
SYMBOL_UP_ARROW:str = "\u2B06"  # up arrow


EVENT_UNKNOWN:int = 0
EVENT_LEVEL:int = 1
EVENT_COMMUNICATION:int = 2


class TelegramDecodePost(object):
    def __init__(self, m: types.Message):
        self.var_data = None
        self.is_forward = None

        if m.reply_to_message:
            return
        elif m.forward_from_chat and m.forward_signature:
            time = m.forward_date
            channel_id = m.forward_from_chat.id
            channel_name = m.forward_from_chat.title
            message_id = m.forward_from_message_id
            bot_name = m.forward_signature
            self.is_forward = True
        elif m.author_signature:
            time = m.date
            channel_id = m.chat.id
            channel_name = m.chat.title
            message_id = m.message_id
            bot_name = m.author_signature
            self.is_forward = False
        else:
            return

        # Splitting the text into lines
        lines = m.text.split("\n")

        match = re.search(r'Nome:\s*"([^"]+)"', lines[0])
        if match:
            device_name = match.group(1).strip()
            result = TelegramSetValues(
                device_name=device_name,
                time=time,
                channel_id=channel_id,
                channel_name=channel_name,
                message_id=message_id,
                bot_name=bot_name,
            )

            log_values = lines[1:]
            # Parsing the lines
            for line in log_values:
                key_value = line.split(":")
                if len(key_value) == 2:
                    try:
                        key = key_value[0].strip()
                        value = re.search(
                            r"-?\d+(\.\d+)?", key_value[1].strip()
                        ).group()
                        result.set_value(key, value)
                    except:
                        pass

            self.var_data = result

        else:
            if len(lines) >= 2:
                splitted = lines[0].split(":")

                if len(splitted) == 2:
                    device_name = splitted[0].strip()
                    text_of_alert = splitted[1].strip()
                    if (
                        len(device_name) > 0
                        and len(text_of_alert) > 0
                    ):

                        event_flag = ''.join([
                            key for key in text_of_alert if key in [
                                SYMBOL_CHECK,
                                SYMBOL_WARNING,
                                SYMBOL_DOWN_ARROW,
                                SYMBOL_UP_ARROW,
                            ]
                        ])
                        if not len(event_flag):
                            return

                        event_type = EVENT_UNKNOWN
                        event_text = lines[1].strip()
                        if "nível" in event_text:
                            event_type = EVENT_LEVEL
                        elif "comunicação" in event_text:
                            event_type = EVENT_COMMUNICATION
                        else:
                            return

                        event_text = f"{lines[0]}\n{lines[1]}"
                        event_text_entities = None
                        try:
                            event_text_entities = [m.entities[0]]
                        except:
                            pass

                        self.var_data = TelegramEvents(
                            device_name=device_name,
                            event_flag=event_flag,
                            time=time,
                            channel_id=channel_id,
                            channel_name=channel_name,
                            message_id=message_id,
                            bot_name=bot_name,
                            event_type=event_type,
                            event_text=event_text,
                            event_text_entities=event_text_entities
                        )
