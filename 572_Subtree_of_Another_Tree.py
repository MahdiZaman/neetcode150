from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif subRoot is None:
            return True
        elif root is None:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or 
                    self.isSubtree(root.right, subRoot))

        # return False

    def sameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        elif p.val != q.val:
            return False
        
        return (self.sameTree(p.left, q.left) and 
                self.sameTree(p.right, q.right))

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    print(sol.isSubtree(root, subRoot)) # Output: True    
    
    # testcase where my first solution failed:
    root = TreeNode(1, TreeNode(1))
    subRoot = TreeNode(1)
    print(sol.isSubtree(root, subRoot)) # Output: True

        