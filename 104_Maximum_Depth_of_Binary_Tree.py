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
        
        ## 3. Iterative Solution (Stack, DFS, root->left->right traversal)
        if not root:
            return 0
        
        res = 1
        stack = [[root, 1]]

        while (stack):
            for i in range(len(stack)):
                node, dep = stack.pop()
                if node:
                    # if node.left:
                    res = max(res, dep)
                    stack.append([node.left, res+1])
                    # if node.right:
                    stack.append([node.right, res+1])
        return res


        # ## 2. Iterative Solution (Deque, BFS. root->left->right traversal)
        # if not root:
        #     return 0
        
        # res = 0
        # q = deque([root])
        # while (q):
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res += 1
        # return res
        

        # ## 1. Recursive Solution
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.maxDepth(root)) # Expected Output: 3
    
'''
# ---------------- Notes from Leetcode ----------------
#### 1. Recursive Solution:
- In recursive, the first thoughts should be around the base case. Consider what happens if (1) the root is empty, (2) root is not empty, but no children. This should draw a picture on the bottom-most 2 levels of the tree. Derive how to get from level[-1] to level[-2]. This should give away what should be kept on doing to reach the top of the tree. 

#### 2. Iterative Solution (BFS) notes:
- use of double-ended queue (deque([..]))
- With deque(), the BFS traversal is intuitive. 
	- initialize with root
	- At each step, pop the node from left (which is root now), and append it's children. 
	- Keep doing this for the length of q
- Keep doing this until there is no more element in q. 


#### 3. Iterative Solution (DFS) notes:
- use of stack
- Stack can be useful for DFS (consider root->left->left->left.....comes back to root, then go right->left->left->...)
	- So appending a node to stack, taking it as a root in next iter by popping it and then appending it's children to the same stack --> If this is how I want to traverse the tree, Stack is useful 
- Also, for problems where a depth/count is related, I can build each element of the stack as a 2-element array. This allows running computation in iterative progressions and allows easy returning the last stage of the the running result. 
**Special Caveat for this problem**
Since we're computing depth, which does not change based on whether a node has only a left child or only a right child or both. Hence the order of traversal (root->left->right vs root->right->left) does not matter in this problem. The current soln actually traverses in the 2nd way). 
'''