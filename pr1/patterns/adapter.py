"""Адаптер: узгоджує несумісний інтерфейс із потрібним."""
class LegacyTemperatureSensor:
    def temperature_fahrenheit(self): return 77.0

class CelsiusSensor:
    def __init__(self, legacy): self.legacy = legacy
    def temperature_celsius(self):
        return (self.legacy.temperature_fahrenheit() - 32) * 5 / 9

if __name__ == "__main__":
    print(f"{CelsiusSensor(LegacyTemperatureSensor()).temperature_celsius():.1f} °C")
