"""Легковаговик: ділить спільний внутрішній стан між об'єктами."""
class TreeType:
    def __init__(self, name, color): self.name, self.color = name, color
class TreeFactory:
    _types = {}
    @classmethod
    def get_type(cls, name, color):
        return cls._types.setdefault((name, color), TreeType(name, color))
class Tree:
    def __init__(self, x, y, kind): self.x, self.y, self.kind = x, y, kind

if __name__ == "__main__":
    oak1, oak2 = TreeFactory.get_type("дуб", "зелений"), TreeFactory.get_type("дуб", "зелений")
    print(Tree(1, 2, oak1).kind is Tree(4, 5, oak2).kind)
