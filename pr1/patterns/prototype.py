"""Прототип: новий об'єкт створюється копіюванням зразка."""
import copy
from dataclasses import dataclass

@dataclass
class Document:
    title: str
    tags: list[str]
    def clone(self): return copy.deepcopy(self)

if __name__ == "__main__":
    original = Document("Звіт", ["чернетка"])
    copy_document = original.clone()
    copy_document.tags.append("готово")
    print(original)
    print(copy_document)
