class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(parent, vals):
    n = len(parent)
    if n == 0:
        return None
    
    # Create nodes for each index
    nodes = [TreeNode(vals[i]) for i in range(n)]
    
    # Identify root (where parent[i] = -1)
    root = None
    for i in range(n):
        if parent[i] == -1:
            root = nodes[i]
            break
    
    # Build tree by assigning children
    for i in range(n):
        if parent[i] != -1:
            # Assign as left or right child of parent
            parent_node = nodes[parent[i]]
            if parent_node.left is None:
                parent_node.left = nodes[i]
            elif parent_node.right is None:
                parent_node.right = nodes[i]
    
    return root

def dfs(root):
    result = []
    def dfs_helper(node):
        if not node:
            return
        result.append(node.val)
        dfs_helper(node.left)
        dfs_helper(node.right)
    dfs_helper(root)
    return result

def bfs(root):
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def tree_traversals(parent, vals):
    # Construct the tree
    root = construct_tree(parent, vals)
    # Perform DFS and BFS
    dfs_result = dfs(root)
    bfs_result = bfs(root)
    return dfs_result, bfs_result

# Example usage:
parent = [-1, 0, 0, 1, 1, 2, 2]
vals = [1, 2, 3, 4, 5, 6, 7]
dfs_result, bfs_result = tree_traversals(parent, vals)
print("DFS:", dfs_result)  # Expected: [1, 2, 4, 5, 3, 6, 7]
print("BFS:", bfs_result)  # Expected: [1, 2, 3, 4, 5, 6, 7]