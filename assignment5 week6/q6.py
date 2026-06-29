import random


class Playlist:
    def __init__(self):
        self.songs = []

    def shuffle(self):
        random.shuffle(self.songs)


my_playlist = Playlist()
my_playlist.songs.append({"title": "Hard Times", "artist": "Paramore"})
my_playlist.songs.append({"title": "Solo", "artist": "Future"})
my_playlist.songs.append({"title": "Shabang", "artist": "Drake"})
my_playlist.songs.append({"title": "A lot", "artist": "21 savage"})
my_playlist.songs.append({"title": "Lonely", "artist": "Akon"})

my_playlist.shuffle()

for song in my_playlist.songs:
    print(f"Title: {song['title']}, Artist: {song['artist']}")