# the ability to create
# https://docs.python.org/3/library/pickle.html
# https://docs.python.org/3/library/shelve.html#module-shelve
# https://code.activestate.com/recipes/576642/
# SO after reading around the plan is to have Persistent Dict
# that allows multiple people reading but only one writing.
# so to write, you have to get a lock
# all graph objects would be just Persistant dict key object

import pickle
import shelve


class Graph:
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
