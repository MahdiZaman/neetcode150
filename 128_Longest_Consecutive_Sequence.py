class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numset = set(nums)
        res = 0

        for i, n in enumerate(nums):
            currLen = 0
            if (n-1) not in numset:
                # currLen = 0
                while (n+currLen) in numset:
                    currLen += 1
            res = max(res, currLen)
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(nums)) # Expected: 4 for [1,2,3,4]
    
'''
Reminder:
**Set** is very powerful for dealing with **unsorted arrays** where input size is high + O(n) is expected but a lot of lookup makes the smallest subtask easy. 
'''