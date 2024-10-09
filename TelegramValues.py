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
        return (
            f"{super().__str__()}"
            f"  level: {self.level}\n"
            f"  raw_level: {self.raw_level}\n"
            f"  distance: {self.distance}\n"
            f"  t0: {self.t0}\n"
            f"  t1: {self.t1}\n"
            f"  v0: {self.v0}\n"
            f"  v1: {self.v1}\n"
            f"  snr: {self.snr}\n"
            f"  rssi: {self.rssi}\n"
            f"  snr_gw: {self.snr_gw}\n"
            f"  rssi_gw: {self.rssi_gw}\n"
            f"  speed1: {self.speed1}\n"
            f"  speed2: {self.speed2}"
        )
