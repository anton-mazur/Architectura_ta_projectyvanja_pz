"""Абстрактна фабрика: створює сумісні сімейства об'єктів."""
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self): pass
class WindowsButton(Button):
    def paint(self): return "Windows button"
class MacButton(Button):
    def paint(self): return "Mac button"
class Checkbox(ABC):
    @abstractmethod
    def paint(self): pass
class WindowsCheckbox(Checkbox):
    def paint(self): return "Windows checkbox"
class MacCheckbox(Checkbox):
    def paint(self): return "Mac checkbox"

class GUIFactory(ABC):
    @abstractmethod
    def button(self): pass
    @abstractmethod
    def checkbox(self): pass
class WindowsFactory(GUIFactory):
    def button(self): return WindowsButton()
    def checkbox(self): return WindowsCheckbox()
class MacFactory(GUIFactory):
    def button(self): return MacButton()
    def checkbox(self): return MacCheckbox()

if __name__ == "__main__":
    ui = MacFactory()
    print(ui.button().paint(), "|", ui.checkbox().paint())
