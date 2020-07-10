from .graph import Graph
from typing import List


class Undirected(Graph):
    def __init__(self, number_of_nodes: int, edge_list: List[List[int]]):
        pass

    # functionalists
    def is_it_a_valid_tree(self) -> bool:
        if (
            not self.detect_cycles()
            and len(self.bfs_traversal()) == self.number_of_nodes
        ):
            return True
        return False

    def detect_cycles(self) -> bool:
        pass

    # traversal
    def bfs_traversal(self) -> List[int]:
        pass

    def dfs_traversal(self) -> List[int]:
        pass
