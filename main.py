# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

from src.undirected import Undirected
from src.dag import Dag
from src.grid import Grid
from src.graph import Graph

a = Undirected(2, [[0, 1]])
b = Dag(2, [[0, 1]])
c = Grid([[1, 0, 1]])
d = Graph()

print(a.is_tree())
print(b.topological_sort())
print(c.count_of_connected_components())
print()

a.save_into_storage()
b.save_into_storage()
c.save_into_storage()
# needs to have a RPC server to load/create/read/run_functions/write objects when needs
