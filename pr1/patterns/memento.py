"""Знімок: зберігає та відновлює попередній стан об'єкта."""
class Editor:
    def __init__(self): self.text = ""
    def save(self): return self.text
    def restore(self, snapshot): self.text = snapshot
class History:
    def __init__(self): self.snapshots = []
    def push(self, snapshot): self.snapshots.append(snapshot)
    def undo(self): return self.snapshots.pop()

if __name__ == "__main__":
    editor, history = Editor(), History()
    editor.text = "Версія 1"; history.push(editor.save())
    editor.text = "Версія 2"; editor.restore(history.undo())
    print(editor.text)
