from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        sum = 0

        candidates.sort() 
    
        def backtrack(i, curr, sum):
            # print(i, curr, sum)
            # base case
            if sum == target: # and curr not in result:
                result.append(curr[::])
                return
            if sum > target or i == len(candidates):
                return

            curr.append(candidates[i])
            backtrack(i+1, curr, sum+candidates[i])

            curr.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, curr, sum)

        backtrack(0, curr, sum)
        return result
    

    
if __name__ == '__main__':
    sol = Solution()
    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 30
    
    print(sol.combinationSum2(candidates, target))