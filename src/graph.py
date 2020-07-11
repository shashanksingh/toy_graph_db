# the ability to create
import pickle


class Graph:
    def __init__(self):
        pass

    def save_into_storage(
        self, database_name: str, table_name: str, object_to_be_stored: object
    ) -> bool:
        relative_path = f"{database_name}_{table_name}_{self.__hash__()}"
        with open(relative_path, "wb") as f:
            pickle.dump(object_to_be_stored, f, pickle.HIGHEST_PROTOCOL)

    def load_from_storage(self, database_name: str, table_name: str) -> object:
        relative_path = f"{database_name}_{table_name}"
        with open(relative_path, "rb") as f:
            data = pickle.load(f)
