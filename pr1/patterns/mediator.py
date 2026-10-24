"""Посередник: централізує зв'язки між компонентами."""
class ChatRoom:
    def send(self, sender, text):
        for user in self.users:
            if user is not sender: user.receive(sender.name, text)
    def __init__(self): self.users = []
    def add(self, user): self.users.append(user); user.room = self
class User:
    def __init__(self, name): self.name, self.room = name, None
    def send(self, text): self.room.send(self, text)
    def receive(self, sender, text): print(f"{self.name} отримав від {sender}: {text}")

if __name__ == "__main__":
    chat = ChatRoom(); anna, bohdan = User("Анна"), User("Богдан")
    chat.add(anna); chat.add(bohdan); anna.send("Привіт!")
