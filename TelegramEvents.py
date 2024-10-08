from TelegramId import TelegramId


class TelegramEvents(TelegramId):
    def __init__(self, event_type: int, event_text: str, event_flag: str = "", event_text_entities = None, **kwargs):
        super().__init__(**kwargs)  # Passa argumentos adicionais para a classe pai
        self.type = event_type
        self.flag = event_flag
        self.text = event_text
        self.text_entities = event_text_entities

    def __str__(self):
        return (
            f"{super().__str__()}"
            f"  type: {self.type}\n"
            f"  flag: {self.flag}\n"
            f"  text: {self.text}\n"
            f"  text_entities: {self.text_entities}\n"
        )
