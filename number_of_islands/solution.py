from collections import deque
DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
class Solution:
    """
    https://www.lintcode.com/problem/433/?_from=collection&fromId=161
Algorithms
Easy
Accepted Rate
36%

Description
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Example 1:

Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
Example 2:

Input:
[
  [1,1]
]
Output:
1
Tags
Breadth First Search/BFS
Union Find
Related Problems
860
Number of Distinct Islands
Medium
804
Number of Distinct Islands II
Hard
677
Number of Big Islands
Medium
663
Walls and Gates
Medium
477
Surrounded Regions
Medium
434
Number of Islands II
Medium

    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # 特殊情况处理
        if not grid or not grid[0]:
            return 0
        islands = 0
        #  if visited, should not be visited twice
        visited = set()
        # traverse every pt in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if is sea, no need to bfs
                # if visited, skip
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands

    def bfs(self, grid, x, y, visited):
        # start from 1 tile: bfs traverse entire island
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            # traverse each direction
            for dx, dy in DIRECTIONS:
                next_x = x + dx
                next_y = y + dy
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        # if out of bounds return false
        if not (0 <= x < n and 0 <= y < m):
            return False
        # if visited, skip: avoid inf loop and redundant bfs variables
        if (x, y) in visited:
            return False
        # if 1, return True, 0 False
        return grid[x][y]


