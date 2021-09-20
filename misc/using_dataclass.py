from dataclasses import dataclass



@dataclass
class Artist:
    name: str

@dataclass
class Album:
    name: str
    artist: Artist
    year: int


artist_1 = Artist('All Them Witches')

albums = [
    Album(name='All Them Witches', artist=artist_1, year=2004),
    Album(name='ATW', artist=artist_1, year=2018)
]

print(albums)
