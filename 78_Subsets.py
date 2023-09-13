from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.subsets(nums)) 
    # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
'''
# Takeaways:
1. What is the **difference** between: **result.append(subset.copy())** and **result.append(subset)**
- when python appends mutable objects like lists: subset.copy() will forward a copy of the subset at that time. But append(subset) will forward a handle/pointer to the original subset. If the subset component changes, result will also change. 
- So append(subset) does not ensure appending what I need at that point in code. Hence sometimes I will need to explicitly append(subset.copy()) instead of just subset. 
- In Recursion, Backtracking (which is multiple concurrent recursions): the difference of appending subset vs subset.copy() is more strongly relevant. 

2. Backtracking:
In backtracking, we use recursive calls to make-and-traverse a tree of possibilities given a list/other data structure. Here in this problem, we have a list, and we want to return all possible subsets of this list. One idea to do this would be finding all possible combinations of the given numbers in the list, and returning the list of all possible combinations, brute force, should work, but not scalable. 
Instead, we would use recursive calls to visit the next component and *visit* the possibilities (1) if we include the next element, (2) if we do not include the next element. In both of these paths, we can consider the next-next element to either include or not include. So we want to go back and forth from each element with all possibilities. For such visiting, Backtracking is a useful technic. 
'''