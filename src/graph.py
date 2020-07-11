from .persistentdictsingleton import PersistentDictSingleton

DATABASE_NAME = "GRAPH"

class Graph:
    def __init__(self):
        self.storage = PersistentDictSingleton()

    def save_into_storage(self):
        database_name = DATABASE_NAME, table_name = self.__hash__()
        self.storage.save_into_storage(database_name, table_name, self)

    #TODO
    def load_from_storage(self):
        database_name = DATABASE_NAME, table_name = self.__hash__()
        self.storage.load_from_storage(database_name, table_name, self)

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__

    def __str__(self) -> str:
        return f"{self.get_class_name()} : {self.__hash__()}"
