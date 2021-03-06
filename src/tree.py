from src.undirected import Undirected
from typing import List

# https://www.youtube.com/watch?v=1XC3p2zBK34


class Tree(Undirected):
    def __init__(self, number_of_nodes: int, edge_list: List[List[int]]):
        super().__init__(number_of_nodes=number_of_nodes, edge_list=edge_list)

    # Tree by 'definition' don't hav cycles so no components
    def find_components(self) -> int:
        return 0

    # Tree by definition don't hav cycles so no components
    def find_components(self) -> List[int]:
        return []
