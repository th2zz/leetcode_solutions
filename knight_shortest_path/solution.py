"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque
# OFFSETS IN 8 DIRECTIONS
OFFSETS = [
    (-2, -1), (-2, 1),
    (-1, 2), (1, 2),
    (2, 1), (2, -1),
    (1, -2), (-1, -2),
        ]
class Solution:
    """https://www.lintcode.com/problem/611/?_from=collection&fromId=161
    TAG: NetEase
    Description
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.

source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
Example 2:

Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output:-1

    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        queue = collections.deque([(source.x, source.y)])
        distance_map = {(source.x, source.y): 0}
        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance_map[(x, y)]
            for dx, dy in OFFSETS:
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(next_x, next_y, grid):
                    continue
                # if visited
                if (next_x, next_y) in distance_map:
                    continue
                queue.append((next_x, next_y))
                distance_map[(next_x, next_y)] = distance_map[(x, y)] + 1
        # unreachable
        return -1

    def is_valid(self, x, y, grid):
        # return false if x,y out of bouds or is unreachable, or is on a barrier
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return not grid[x][y]

