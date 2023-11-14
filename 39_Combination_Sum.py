from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def dfs(idx, cur, sum):
            if sum == target:
                result.append(cur.copy())
                return
            if sum > target:
                return
            if idx >= len(candidates):
                return
            
            cur.append(candidates[idx])
            dfs(idx, cur, sum + candidates[idx])
            
            cur.pop()
            dfs(idx + 1, cur, sum)

        dfs(0, [], 0)
        return result
    
if __name__ == '__main__':
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(sol.combinationSum(candidates, target)) 
    # Output: [[2, 2, 3], [7]]
    
''' For backtracking problems, the first challenge is to understand the need of **walking down a decision tree** for solving the problem. 
    - In this problem, the same number can be included unlimited times. So there's no way we can do an element-wise traversal to compute the total for all possible combinations. 
    - So an idea is that: at any index, consider two options: 
        - include *number at current idx*, 
        - Do NOT include *number at current idx*. 
    - Each path gives two options, and from each of the paths we can consider 
        - if current sum is equal to target, this is a valid combination. 
        - if current sum crossed target, this path is not going to give any more meaningful combination.
        - if the index I am about to handle has crossed the number of elements in given candidate array, this path is not going to give any more meaningful combination. 
    - So from each of the paths, we can consider:
        - either to: stay at current idx to consider this number more times (because surely the sum has not reached target yet). 
        - or: do not include the *number at current index*. Instead move to the next index, and then work with that number.'''