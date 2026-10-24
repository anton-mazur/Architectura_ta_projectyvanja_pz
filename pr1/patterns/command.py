"""Команда: перетворює дію на самостійний об'єкт."""
class Light:
    def on(self): return "Світло увімкнено"
    def off(self): return "Світло вимкнено"
class LightCommand:
    def __init__(self, light, action): self.light, self.action = light, action
    def execute(self): return getattr(self.light, self.action)()
class Remote:
    def submit(self, command): return command.execute()

if __name__ == "__main__":
    print(Remote().submit(LightCommand(Light(), "on")))
