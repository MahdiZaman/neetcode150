from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False
        
        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1

        min_nums = list(count.keys())
        heapq.heapify(min_nums)

        while min_nums:
            first = min_nums[0]
            for num in range(first, first + groupSize):
                print(num)
                if num not in count:
                    return False
                count[num] -= 1
                if count[num] == 0:
                    if num != min_nums[0]:
                        return False
                    # del count[num]
                    heapq.heappop(min_nums)
                # heapq.heappop(min_nums)
        return True


if __name__ == '__main__':
    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 3
    solution = Solution()
    print(solution.isNStraightHand(hand, groupSize)) # True
    # print(solution.can_attend_meetings(intervals2)) # True