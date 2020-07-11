import pickle
import shelve


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
        pass

    def save_into_storage(
        self, database_name: str, table_name: str, object_to_be_stored: object
    ) -> bool:
        relative_path = f"{database_name}_{table_name}"
        with open(relative_path, "wb") as f:
            pickle.dump(object_to_be_stored, f, pickle.HIGHEST_PROTOCOL)

    def load_from_storage(self, database_name: str, table_name: str) -> object:
        relative_path = f"{database_name}_{table_name}"
        with open(relative_path, "rb") as f:
            data = pickle.load(f)
