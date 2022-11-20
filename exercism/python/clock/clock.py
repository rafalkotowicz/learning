class Clock:
    def __init__(self, hour, minute):
        self.minutes = minute % 60
        self.hour = (hour + minute // 60) % 24

    def __repr__(self) -> str:
        return f"Clock({self.hour}, {self.minutes})"

    def __str__(self) -> str:
        hour: str = f"0{self.hour}" if self.hour < 10 else self.hour
        minute: str = f"0{self.minutes}" if self.minutes < 10 else self.minutes
        return f"{hour}:{minute}"

    def __eq__(self, other) -> bool:
        return self.hour == other.hour and self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(self.hour, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minutes - minutes)
