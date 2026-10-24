"""DIP: високорівневі модулі залежать від абстракцій, а не реалізацій."""
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient: str, text: str) -> str: pass

class EmailSender(MessageSender):
    def send(self, recipient, text): return f"Email для {recipient}: {text}"

class SmsSender(MessageSender):
    def send(self, recipient, text): return f"SMS для {recipient}: {text}"

class NotificationService:
    def __init__(self, sender: MessageSender): self.sender = sender
    def notify(self, recipient, text): return self.sender.send(recipient, text)

if __name__ == "__main__":
    print(NotificationService(EmailSender()).notify("student@example.com", "Завдання готове"))
    print(NotificationService(SmsSender()).notify("+380000000000", "Завдання готове"))
