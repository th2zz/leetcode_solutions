"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
import collections


class Solution:
    """https://www.lintcode.com/problem/127/?_from=collection&fromId=161
    Description
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

You can assume that there is at least one topological order in the graph.
Learn more about representation of graphs

The number of graph nodes <= 5000
Example
Example 1:

Input:

graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}
Output:

[0, 1, 2, 3, 4, 5]
Explanation:

For graph as follow:

图片

he topological order can be:
[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
You only need to return any topological order for the given graph.

Challenge
Can you do it in both BFS and DFS?
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # 1. get statistics on indegree
        node_to_indegree = self.get_indgree(graph)
        # 2. add all source as starting nodes
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        # res
        order = []
        # 3. keep removing source and its connecting edges, all connected nodes indegree -1
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                # 4. if found new source add to queue
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order

    def get_indgree(self, graph):
        pass