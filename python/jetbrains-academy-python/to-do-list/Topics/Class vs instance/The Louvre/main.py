class Painting:
    museum = "Louvre"

    def __init__(self, title=None, artist=None, year=None):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.artist} ({self.year}) hangs in the ' \
               f'{Painting.museum}.'


print(Painting(input(), input(), input()))
