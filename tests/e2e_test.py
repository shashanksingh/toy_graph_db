# TBD
from src.undirected import Undirected
from src.dag import Dag
from src.grid import Grid
from src.graph import Graph
from src.tree import Tree

a = Undirected(2, [[0, 1]])
b = Dag(2, [[0, 1]])
c = Grid([[1, 0, 1]])
d = Graph()
e = Tree(2, [[0, 1]])

print(a.is_tree())
print(b.topological_sort())
print(c.count_of_connected_components())
print()

a.save_into_storage()
b.save_into_storage()
c.save_into_storage()
e.save_into_storage()
print(d.list_all())