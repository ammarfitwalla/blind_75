"""
98. Validate Binary Search Tree (Medium)
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

use valid as dfs and use -/+ inf
"""

# Definition for a binary tree node.
from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root, min = -math.inf, max = math.inf):
        
        if root is None:
            return True
        if root.val > min and root.val < max:
            return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)
        return False