import collections

#
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    """Description
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.

You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.

You need return the node with the same label as the input node.
How we represent an undirected graph: http://www.lintcode.com/help/graph/

Example
Example1

Input:
{1,2,4#2,1,4#4,1,2}
Output:
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2
 \     |
  \    |
   \   |
    \  |
      4

    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        if not node:
            return None
        nodes = self.find_nodes_by_bfs(node)
        mapping = self.copy_nodes(nodes)
        self.copy_edges(nodes, mapping)
        return mapping[node]

    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        # 用于保存所有点 不重不漏
        visited = set([node])
        while queue:
            curt_node = queue.popleft()
            for neighbor in curt_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return list(visited)

    def copy_nodes(self, nodes):
        # {old node -> new node} mapping relation
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping

    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            # copy neighbors record for each node ( equivalent to copy edges )
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
