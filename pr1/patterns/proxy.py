"""Замісник: контролює доступ до реального об'єкта."""
class Database:
    def query(self): return "Конфіденційні дані"
class DatabaseProxy:
    def __init__(self, user): self.user, self.database = user, Database()
    def query(self):
        if self.user != "admin": return "Доступ заборонено"
        return self.database.query()

if __name__ == "__main__":
    print(DatabaseProxy("guest").query())
    print(DatabaseProxy("admin").query())
