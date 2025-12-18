"""
212. Word Search II (Hard)

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

(word search + Trie Prefix Tree)
"""

from typing import List



class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""
    
    def addWord(self, word):
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()
        
        def dfs(r, c, node):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or board[r][c] not in node.children:
                return
            
            if node.children[board[r][c]].word:
                res.add(node.children[board[r][c]].word)
                node.children[board[r][c]].word = ""
            visited.add((r, c))
            node = node.children[board[r][c]]
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return list(res)