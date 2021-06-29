"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """ https://www.lintcode.com/problem/902/?_from=collection&fromId=161
    Description
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example
Example 1:

Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.
Example 2:

Input：{2,1,3},1
Output：1
Explanation：
  2
 / \
1   3
The first smallest element is 1.
Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def push_all_left_side_nodes(self, node, stack):
        while node:
            stack.append(node)
            node = node.left
        return node  # last node

    def kthSmallest1(self, root, k):  # regular non-recursive binary tree traversal
        stack = []
        self.push_all_left_side_nodes(root, stack)
        for i in range(k - 1):  # k-1 operations in 0 ... k-2; this is to make the kth number at stack top
            node = stack.pop()
            if node.right:
                self.push_all_left_side_nodes(node.right, stack)
        return stack[-1].val

    def kthSmallest(self, root, k):  # this one can do binary tree traversal in different directions
        stack = []
        self.push_all_left_side_nodes(root, stack)
        for i in range(k - 1):
            node = stack[-1]
            if node.right:
                self.push_all_left_side_nodes(node.right, stack)
            else:
                node = stack.pop(-1)
                while stack and stack[-1].right == node:  # 只要刚pop的节点是当前栈顶right child  keep popping
                    node = stack.pop(-1)  # when this stop, the node we just popped is a left child of stack top
        return stack[-1].val
