from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.nums = nums
        self.k = k
        self.heap = nums[:self.k] # [0] * k
        
        ### this was throwing error when k is larger than len(nums) for the 10th testcase
        ### ["KthLargest","add","add","add","add","add"]
        ### [[3,[5,-1]],[2],[1],[-1],[3],[4]]
        # if self.k <= 0 or len(nums) < self.k:
        #     return
        
        heapq.heapify(self.heap)

        for num in nums[self.k:]:
            heapq.heappush(self.heap, num)
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # if len(self.heap) > 0 and val > self.heap[0]:
        if len(self.heap) > self.k :
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == '__main__':
    obj = KthLargest(3, [4,5,8,2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))