"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys


class Solution:
    """ https://www.lintcode.com/problem/596/?_from=collection&fromId=161
    Description
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
The range of input and output data is in int.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.

Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.

    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        minimum, subtree, sum_of_root = self.get_min_tree_sum(root)
        return subtree

    def get_min_tree_sum(self, root):
        # return 最小和 最小子树根 当前树之和
        if not root:
            return sys.maxsize, None, 0
        # left subtree sum
        left_min, left_subtree, left_sum = self.get_min_tree_sum(root.left)
        # right subtree sum
        right_min, right_subtree, right_sum = self.get_min_tree_sum(root.right)
        # current tree sum
        sum_of_root = left_sum + root.val + right_sum
        min_sum = min(left_min, right_min, sum_of_root)
        # case 1. left subtree sum is minimum
        if left_min == min_sum:
            return left_min, left_subtree, sum_of_root
        # case 2. right subtree sum is minimum
        if right_min == min_sum:
            return right_min, right_subtree, sum_of_root
        # case 3. current tree sum is minimum
        return sum_of_root, root, sum_of_root
