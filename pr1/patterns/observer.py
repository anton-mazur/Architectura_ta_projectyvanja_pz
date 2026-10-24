"""Спостерігач: підписники отримують повідомлення про зміни."""
class WeatherStation:
    def __init__(self): self.observers = []
    def subscribe(self, observer): self.observers.append(observer)
    def set_temperature(self, value):
        for observer in self.observers: observer(value)

if __name__ == "__main__":
    station = WeatherStation()
    station.subscribe(lambda t: print(f"Дисплей: {t} °C"))
    station.subscribe(lambda t: print("Холодно" if t < 10 else "Тепло"))
    station.set_temperature(8)
