from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def calc_depth(node):
            if not node:
                return 0
            
            left = calc_depth(node.left)
            right = calc_depth(node.right)

            if abs(left - right) > 1:
                return -1
            
            if min(left,right) == -1:
                return -1

            return 1 + max(left, right)
        
        return calc_depth(root) != -1
    
    

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.isBalanced(root)) # Output: True
    
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(4)), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    print(sol.isBalanced(root)) # Output: False
    
    