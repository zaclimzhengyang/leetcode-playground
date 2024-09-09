'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
'''
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        create a result variable that is a list of int
        since both root1 and root2 might not be the same, we have to traverse both separately
        recursively traverse to the left, until we ensure that it is a leaf node -> append the node val to result
        then traverse to the right, append the node val to result
        repeat the steps for root2, store node values in result2
        return result == result2
        '''
        result1: List[int] = []
        result2: List[int] = []

        self.traverse_and_append(root1, result1)
        self.traverse_and_append(root2, result2)

        return result1 == result2

    def is_leaf_node(self, root: Optional[TreeNode]) -> bool:
        return root is not None and root.left is None and root.right is None

    def traverse_and_append(self, root: Optional[TreeNode], result: List[int]) -> None:
        if root is None:
            return
        if self.is_leaf_node(root):
            result.append(root.val)
            return
        if root.left is not None:
            self.traverse_and_append(root.left, result)
        if root.right is not None:
            self.traverse_and_append(root.right, result)
