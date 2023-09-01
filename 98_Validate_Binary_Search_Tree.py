from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            return check(node.left, left, node.val) and check(node.right, node.val, right)

        return check(root, float('-inf'), float('inf'))
    
    
if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(sol.isValidBST(root)) # Output: True
    
    
'''
##### Definition of Binary Search Tree
- **ALL** nodes on **left** subtree should have values **less** than current node
- **ALL** nodes on **right** subtree should have values **larger** than current node

- So when using a recursive method, it is not enough to compare the current node's value to it's children. 
- We also need to keep track of **max** allowed value on the left subtree and **min** allowed value on the right subtree
	- In other words, we need to keep track of a range for both subtrees. The edge of the ranges can be forwarded to a child via the recursive function param.


Misc Note:
- 'Inf' can be misinterpreted by python. It is safer to use explitict float conversion eg float('-inf')) and float('inf')) 
'''