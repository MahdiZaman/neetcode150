from typing import (
    List,
)
# from lintcode import (
#     Interval,
# )

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals) -> bool:
        # Write your code here
        intervals.sort()
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= lastEnd:
                continue
            else:
                return False
        return True
    
    
if __name__ == '__main__':
    intervals = [(0,30),(5,10),(15,20)]
    intervals2 = [(5,8),(9,15)] 
    
    solution = Solution()
    print(solution.can_attend_meetings(intervals)) # False
    # print(solution.can_attend_meetings(intervals2)) # True