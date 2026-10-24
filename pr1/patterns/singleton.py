"""Одинак: клас має лише один спільний екземпляр."""
class Settings:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.language = "uk"
        return cls._instance

if __name__ == "__main__":
    first, second = Settings(), Settings()
    second.language = "en"
    print(first is second, first.language)
