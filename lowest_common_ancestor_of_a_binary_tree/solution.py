"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """https://www.lintcode.com/problem/88/?_from=collection&fromId=161
    Description
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

Assume two nodes are exist in tree.

Example
Example 1:

Input:

tree = {1}
A = 1
B = 1
Output:

1
Explanation:

For the following binary tree（only one node）:
        1
LCA(1,1) = 1
Example 2:

Input:

tree = {4,3,7,#,#,5,6}
A = 3
B = 5
Output:

4
Explanation:

For the following binary tree:

     4
    / \
   3   7
      / \
     5   6

LCA(3, 5) = 4
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        if not root:
            return root
        if root == A or root == B:
            return root
        left = self.lowestCommonAncestor(root.left, A, B)  # go find A or B in left and right
        right = self.lowestCommonAncestor(root.right, A, B)
        if left and right:  # if found at both sides: root is lca
            return root
        if left:  # left subtree is one node or lca in left subtree (A and B both in the left)
            return left
        if right:  # right subtree is one node or lca in the right subtree (A and B both in the right)
            return right
        return None  # non-existent / left right both none
