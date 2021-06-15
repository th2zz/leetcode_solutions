class Solution:
    """
    Description
给一个 01 矩阵，求不同的岛屿的个数。

0 代表海，1 代表岛，如果两个 1 相邻，那么这两个 1 属于同一个岛。我们只考虑上下左右为相邻。

Example
样例 1：

输入：
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
输出：
3
样例 2：

输入：
[
  [1,1]
]
输出：
1

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


