class SpaceAge:
    SECONDS_IN_EARTH_YEAR = 31_557_600

    to_earth = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.__seconds_to_year__() / SpaceAge.to_earth["mercury"], 2)

    def on_venus(self):
        return round(self.__seconds_to_year__() / SpaceAge.to_earth["venus"], 2)

    def on_earth(self):
        return round(self.__seconds_to_year__() / SpaceAge.to_earth["earth"], 2)

    def on_mars(self):
        return round(self.__seconds_to_year__() / SpaceAge.to_earth["mars"], 2)

    def on_jupiter(self):
        return round(self.__seconds_to_year__() / SpaceAge.to_earth["jupiter"], 2)

    def on_saturn(self):
        return round(self.__seconds_to_year__() / SpaceAge.to_earth["saturn"], 2)

    def on_uranus(self):
        return round(self.__seconds_to_year__() / SpaceAge.to_earth["uranus"], 2)

    def on_neptune(self):
        return round(self.__seconds_to_year__() / SpaceAge.to_earth["neptune"], 2)

    def __seconds_to_year__(self):
        return self.seconds / SpaceAge.SECONDS_IN_EARTH_YEAR
