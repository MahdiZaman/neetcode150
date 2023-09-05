from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## Recursive
        res = 0
        idx = 0

        def check(node):
            nonlocal res, idx
            
            if not node:
                return
            
            check(node.left)

            idx += 1
            if idx == k:
                res = node.val
            
            check(node.right)
        
        check(root)
        return res
            
        ## Iterative DFS
        # curr = root
        # stack = []
        # n = 0

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     n += 1
        #     if n==k:
        #         return curr.val
        #     curr = curr.right
        
if __name__ == '__main__':
    sol = Solution()
    # root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    # k = 1
    # print(sol.kthSmallest(root, k)) # Output: 1
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    k = 3
    print(sol.kthSmallest(root, k)) # Output: 3

'''
##### Take-away (Iterative soln):
- stack is useful to iteratively traverse Binary Search Trees. 
	- Two nested while loops with a stack is useful tool for this
	- inner while loop takes care of stacking each node's branches in-order
 
##### Take-away (Recursive soln):
- for recursive soln, we need to keep track of the index of the current node and return the value when the index matches k
- we can use a global variable to keep track of the index
- storing the result can be preferable than returning the result, to avoid confusions with recursive return stack
'''    