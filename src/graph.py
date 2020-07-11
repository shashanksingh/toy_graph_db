from .persistentdictsingleton  import PersistentDictSingleton

class Graph:
    def __init__(self):
        self.storage = PersistentDictSingleton()

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__

    def __str__(self) -> str:
        return f"{self.get_class_name()} : {self.__hash__()}"


