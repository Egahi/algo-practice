'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        EDGES = [(0,1), (1,0), (0,-1), (-1,0)]
        row = len(grid)
        column = len(grid[0])
        visited = set()
        adjancency_list = {}

        def get_neighbours(x, y):
            visited.add((x, y))

            adjancency_list[(x, y)] = []

            for edge in EDGES:
                neighbour = (x+edge[0], y+edge[1])

                if not (0 <= neighbour[0] < row and \
                    0 <= neighbour[1] < column):
                    continue

                if grid[neighbour[0]][neighbour[1]] == '1':
                    adjancency_list[(x, y)].append(neighbour)

            for item in adjancency_list[(x, y)]:
                if item in visited:
                    continue

                get_neighbours(item[0], item[1])

        islands = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] != '1' or (i, j) in visited:
                    continue

                islands += 1
                get_neighbours(i, j)

        return islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

obj = Solution()
print(obj.numIslands(grid))