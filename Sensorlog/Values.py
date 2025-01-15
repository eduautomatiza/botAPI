from Sensorlog.Id import Id


class Values(Id):
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

    def to_json(self):
        # Chama o to_json da classe pai (Id) e adiciona seus próprios atributos
        data = super().to_json()  # Obtém os atributos da classe pai
        data.update({
            "values" : {
                "level": self.level,
                "raw_level": self.raw_level,
                "distance": self.distance,
                "t0": self.t0,
                "t1": self.t1,
                "v0": self.v0,
                "v1": self.v1,
                "snr": self.snr,
                "rssi": self.rssi,
                "snr_gw": self.snr_gw,
                "rssi_gw": self.rssi_gw,
                "speed1": self.speed1,
                "speed2": self.speed2,
            }
        })
        return data