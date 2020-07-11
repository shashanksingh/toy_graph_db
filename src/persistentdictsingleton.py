import pickle
import shelve

FILE_NAME_OF_DB = "WHERE_THE_DOGS_SLEEP"

# the ability to create
# https://docs.python.org/3/library/pickle.html
# https://docs.python.org/3/library/shelve.html#module-shelve
# https://code.activestate.com/recipes/576642/
# SO after reading around the plan is to have Persistent Dict
# that allows multiple people reading but only one writing.
# so to write, you have to get a lock
# all graph objects would be just Persistant dict key object


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class PersistentDictSingleton(metaclass=SingletonMeta):
    def __init__(self):
        self.shelve = shelve.open(FILE_NAME_OF_DB)

    def save_into_storage(
        self, database_name: str, table_name: str, object_to_be_stored: object
    ) -> bool:
        relative_path = f"{database_name}_{table_name}"
        self.shelve[relative_path] = object_to_be_stored

    def load_from_storage(self, database_name: str, table_name: str) -> object:
        relative_path = f"{database_name}_{table_name}"
        return self.shelve[relative_path]

    # TODO : doesnt work , should work though https://stackoverflow.com/a/54667683
    def list_all(self) -> object:
        return [value for key, value in self.shelve.items()]

    def close(self):
        self.shelve.close()
