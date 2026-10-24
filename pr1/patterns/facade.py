"""Фасад: надає простий інтерфейс до складної підсистеми."""
class Projector:
    def on(self): return "Проектор увімкнено"
class SoundSystem:
    def on(self): return "Звук увімкнено"
class StreamingService:
    def play(self, film): return f"Відтворюється: {film}"
class HomeTheater:
    def __init__(self): self.projector, self.sound, self.stream = Projector(), SoundSystem(), StreamingService()
    def watch_movie(self, film): return [self.projector.on(), self.sound.on(), self.stream.play(film)]

if __name__ == "__main__":
    print(*HomeTheater().watch_movie("Дюна"), sep="; ")
