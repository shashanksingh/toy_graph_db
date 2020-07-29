from .persistentdictsingleton import PersistentDictSingleton
from abc import ABCMeta

DATABASE_NAME = "GRAPH"


class Graph(metaclass=ABCMeta):

    # constructor
    def __init__(self):
        pass

    # destructor
    # def __del__(self):
    #     storage = PersistentDictSingleton()
    #     storage.close()

    def __str__(self) -> str:
        return f"{self.get_class_name()} : {self.__hash__()}"

    def save_into_storage(self):
        storage = PersistentDictSingleton()
        database_name, table_name = DATABASE_NAME, self.__hash__()
        storage.save_into_storage(database_name, table_name, self)

    # TODO : Load based on what ?
    def load_from_storage(self):
        storage = PersistentDictSingleton()
        database_name, table_name = DATABASE_NAME, self.__hash__()
        storage.load_from_storage(database_name, table_name, self)

    def list_all(self):
        storage = PersistentDictSingleton()
        return storage.list_all()

    def find(self):
        pass

    def filter(self):
        pass

    def remove(self):
        pass

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__

    @staticmethod
    def whoami():
        return "graph"
