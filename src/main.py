# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

from undirected import Undirected
from dag import Dag
from grid import Grid


a = Undirected(2, [[0, 1]])
b = Dag(2, [[0, 1]])
c = Grid([[1, 0, 1]])

print(a.has_cycles())
print(b.topological_sort())
print(c.count_of_connected_components())

# needs to have a RPC server to load/create/read/run_functions/write objects when needs
