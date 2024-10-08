from TelegramId import TelegramId


class TelegramValues(TelegramId):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Passing additional arguments to the parent class
        self.level: float = None
        self.raw_level: float = None
        self.distance: float = None
        self.t0: float = None
        self.t1: float = None
        self.v0: float = None
        self.v1: float = None
        self.snr: int = None
        self.rssi: int = None
        self.snr_gw: int = None
        self.rssi_gw: int = None
        self.speed1: int = None
        self.speed2: int = None

    def __str__(self):
        return f"  time: {self.time}\n  channel_id: {self.channel_id}\n  channel_name: {self.channel_name}\n  bot_id: {self.bot_id}\n  bot_name: {self.bot_name}\n  device_id: {self.device_id}\n  device_name: {self.device_name}\n  level: {self.level}\n  raw_level: {self.raw_level}\n  distance: {self.distance}\n  t0: {self.t0}\n  t1: {self.t1}\n  v0: {self.v0}\n  v1: {self.v1}\n  snr: {self.snr}\n  rssi: {self.rssi}\n  snr_gw: {self.snr_gw}\n  rssi_gw: {self.rssi_gw}\n  speed1: {self.speed1}\n  speed2: {self.speed2}"
