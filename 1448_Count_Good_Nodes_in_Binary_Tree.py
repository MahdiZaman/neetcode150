# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    count = 0
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return self.count
        self.compare(root, root.val)
        return self.count

    def compare(self, node, max_in_path):
        if not node:
            return
        
        if node.val >= max_in_path:
            max_in_path = node.val
            self.count += 1
        self.compare(node.left, max_in_path)
        self.compare(node.right, max_in_path)
        
if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print(sol.goodNodes(root)) # Output: 4