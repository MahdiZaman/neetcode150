from typing import List
import collections

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # if heights is None:
        #     return None


        nrow, ncol = len(heights), len(heights[0])
        result = []

        

        def bfs(row, col):
            self.pacific = False
            self.atlantic = False
            q = collections.deque()
            q.append([row, col])
            
            while q:
                curr_row, curr_col = q.popleft()
                
                # print(q)
                directions = [[-1,0], [1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = curr_row + dr, curr_col + dc
                    # curr_h = heights[r][c]

                    if 0 <= r < nrow and 0 <= c < ncol and heights[r][c] <= heights[curr_row][curr_col]:
                        q.append([r,c])
                    
                                        
                    if (r < 0 or c < 0):
                        self.pacific = True
                    elif (r >= nrow or c >= ncol):
                        self.atlantic = True
                    

            if self.pacific and self.atlantic:
                result.append([row, col])
                # print(result)
            return

        if not heights or not heights[0]:
            return result

        for row in range(nrow):
            for col in range(ncol):
                bfs(row, col)

        return result
    
# write a testcase for this problem
if __name__=='main':
    s = Solution()
    heights = [[1,2,2,3,5],
               [3,2,3,4,4],
               [2,4,5,3,1],
               [6,7,1,4,5],
               [5,1,1,2,4]]
    print(s.pacificAtlantic(heights)) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    
    