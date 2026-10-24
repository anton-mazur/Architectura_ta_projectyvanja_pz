"""Ітератор: послідовно обходить колекцію, приховуючи її будову."""
class Playlist:
    def __init__(self, songs): self.songs = songs
    def __iter__(self): return PlaylistIterator(self.songs)
class PlaylistIterator:
    def __init__(self, songs): self.songs, self.index = songs, 0
    def __iter__(self): return self
    def __next__(self):
        if self.index >= len(self.songs): raise StopIteration
        song = self.songs[self.index]; self.index += 1
        return song

if __name__ == "__main__":
    for song in Playlist(["Пісня 1", "Пісня 2"]): print(song)
