from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i, v in enumerate(t):
                # print(v)
                if v == target[i]:
                    good.add(i)

        return len(good) == 3
    
    
if __name__=='__main__':
    solution = Solution()
    
    # testcase 1
    triplets = [[2,5,3],[1,8,4],[1,7,5]]
    target = [2,7,5]
    print(solution.mergeTriplets(triplets, target)) # True
    
    # testcase 2
    triplets = [[3,4,5],[4,5,6]]
    target = [3,2,5]
    print(solution.mergeTriplets(triplets, target)) # False
    
    triplets =[[1,3,1]]
    target = [1,3,2]
    print(solution.mergeTriplets(triplets, target)) # False