# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ## 2. Iterative Solution
        if not root:
            return 0
        
        res = 0
        q = deque([root])
        while (q):
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1
        return res


        # ## 1. Recursive Solution
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.maxDepth(root)) # Expected Output: 3