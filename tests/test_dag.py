from unittest import TestCase
from src.dag import Dag


def test_topological_sort():
    dag = Dag(2, [[0, 1]])
    assert dag.topological_sort() == [0, 1]
