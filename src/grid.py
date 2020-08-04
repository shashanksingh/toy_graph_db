from typing import List, Tuple
from collections import deque
from .graph import Graph
from hashlib import md5

EMPTY_VALUE = 0
DEFAULT_VALID_DIRECTION_VECTOR = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # all 4 directions


class Grid(Graph):
    def __init__(self, grid: List[List[int]], valid_direction_vector=None):
        self.grid = grid
        self.visited = set()
        self.maximum_row = len(grid)
        self.maximum_column = len(grid[0])
        if valid_direction_vector is None:
            valid_direction_vector = DEFAULT_VALID_DIRECTION_VECTOR
        self.direction_vector = valid_direction_vector
        super()

    def __hash__(self):
        return hash(str(self.grid))

    def clear_visited(self):
        self.visited = set()

    def count_of_connected_components(self) -> int:
        size_of_visited = 0
        number_of_components = 0
        for row in range(self.maximum_row):
            for column in range(self.maximum_column):
                self.dfs(row, column)
                if size_of_visited != len(self.visited):
                    number_of_components += 1
                    size_of_visited = len(self.visited)
        return number_of_components

    # TODO
    def find_connected_components(self) -> List:
        size_of_visited = 0
        number_of_components = 0
        for row in range(self.maximum_row):
            for column in range(self.maximum_column):
                self.dfs(row, column)
                if size_of_visited != len(self.visited):
                    number_of_components += 1
                    size_of_visited = len(self.visited)
        return number_of_components

    # TODO
    def are_isomorphic(
        self, component_first: List[List[int]], component_second: List[List[int]]
    ):
        pass

    def dfs(self, row, column):
        for row_dv, column_dv in self.direction_vector:
            new_row, new_column = row + row_dv, column + column_dv
            if (
                self.grid[row][column] != EMPTY_VALUE
                and (new_row, new_column) not in self.visited
                and 0 <= new_row < self.maximum_row
                and 0 <= new_column < self.maximum_column
            ):
                self.visited.add((row, column))
                self.dfs(new_row, new_column)

    def bfs(self, row: int, column: int, level: int = 0):
        queue = deque()
        queue.append((row, column, level))

        while len(queue) > 0:
            for elements_count in range(len(queue)):
                row, column, level = queue.popleft()
                for row_dv, column_dv in self.direction_vector:
                    new_row = row + row_dv
                    new_column = column + column_dv
                    new_level = level + 1
                    if (
                        (new_row, new_column) not in self.visited
                        and 0 <= new_row < self.maximum_row
                        and 0 <= new_column < self.maximum_column
                    ):
                        self.visited.add((new_row, new_column))
                        queue.append((new_row, new_column, new_level))
