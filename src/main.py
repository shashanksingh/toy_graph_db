# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

from src.undirected import Undirected
from src.dag import Dag
from src.grid import Grid

a = Undirected(2,[[0,1]])
b = Dag(2,[[0,1]])
c = Grid([[1,0,1]])

print(a.has_cycles())


