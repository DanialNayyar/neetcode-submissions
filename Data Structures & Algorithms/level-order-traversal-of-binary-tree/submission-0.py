#Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        que = deque([root])
        if root is None:
            return []
        while len(que) > 0:
            current_que_size = len(que)
            new_level = []
            for i in range(current_que_size):
                node = que.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        que.append(child)
            
            result.append(new_level)
        
        return result