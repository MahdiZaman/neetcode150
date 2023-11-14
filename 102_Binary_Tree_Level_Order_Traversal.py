from typing import Optional, List 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        queue = deque()
        if root:
            queue.append(root)

        while queue: # each iteration is a level
            curr = []
            print(len(queue))
            for _ in range(len(queue)): # for each node in current level
                node = queue.popleft() # get node, put its children in queue
                curr.append(node.val)
                if node.left: 
                    queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
            result.append(curr)

        return result


if __name__ == '__main__':
    sol = Solution()
    # #case 1
    # root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    # print(sol.levelOrder(root)) # Output: [[3], [9, 20], [15, 7]]
    
    # #case 2
    # root = TreeNode(1)
    # print(sol.levelOrder(root)) # Output: [[1]]
    
    #case 3
    root = None
    print(sol.levelOrder(root)) # Output: []
    
    
### Main Take away:
# - **using a for loop for the length of current queue -- this is handy when I have to keep track when the current-level ends.** Because trees are just root,left,right: there is no inherent way to track the levels. 
# - **appending element is faster in deque** than list-based queue (probably faster than std queue as well)
     