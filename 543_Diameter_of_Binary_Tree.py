from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # need to keep a global variable for diameter
        dia = 0

        def dfs(root):
            nonlocal dia
            # base case
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            dia = max(dia, left + right)
            return 1 + max(left, right)

        dfs(root)
        return dia
    

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    solution = Solution()
    print(solution.diameterOfBinaryTree(root)) # Output: 3

if __name__ == "__main__":
    main()