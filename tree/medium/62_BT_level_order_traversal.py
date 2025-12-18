"""
102. Binary Tree Level Order Traversal (Medium)

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

(use bfs with queue)
"""

# Definition for a binary tree node.
from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        q = collections.deque()
        q.append(root.val)

        while q:
            q_len = len(q)
            levels = []
            for i in q_len:
                node = q.popleft()
                levels.append(node.val)
                q.append(node.right)
                q.append(node.left)
            if levels:
                res.append(levels)

        return res