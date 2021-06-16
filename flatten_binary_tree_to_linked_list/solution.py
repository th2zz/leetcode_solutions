"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """ https://www.lintcode.com/problem/453/?_from=collection&fromId=161
    Description
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Example
Example 1:

Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
Example 2:

Input:{1}
Output:{1}
Explanation：
         1
         1
Challenge
Do it in-place without any extra memory.
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, root):
        if not root:
            return None
        left_last = self.flatten_and_return_last_node(root.left)  # flatten left and right subtree and get last node
        right_last = self.flatten_and_return_last_node(root.right)
        if left_last:  # need to transplant flattened left subtree to root
            left_last.right = root.right
            root.right = root.left
            root.left = None
        # tree at root got flattened, return last node of this tree:
        # logically, priority gives to right last, left last, and finally root
        return right_last or left_last or root
