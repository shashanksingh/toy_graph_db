from src.graph import Graph
from typing import List, Set
from collections import defaultdict

class Directed(Graph):
    def __init__(self, edges: List[List[int]]):
        self.graph = defaultdict(set)  # no duplicates

    def __init__(self, number_of_nodes: int, edges: List[List[int]]):
        self.graph = defaultdict(set)  # no duplicates

    def __hash__(self):
        return hash(str(self.graph))

    def dfs_on_edges(self, source: int, target: int, seen: Set) -> bool:
        if source not in seen:
            seen.add(source)
            if source == target:
                return True
            return any(self.dfs(kid, target, seen) for kid in self.graph[source])
