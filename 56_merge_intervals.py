class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])    ## this is the key part in this problem 
                                                ## to avoid O(n^2) and do in O(nlogn)

        output = [intervals[0]]
        # print(output)

        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])

        return output
