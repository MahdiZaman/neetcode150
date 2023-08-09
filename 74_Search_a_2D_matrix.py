from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        nrow, ncol = len(matrix), len(matrix[0])
        print(nrow, ncol)
        i = 0
        while i<nrow and matrix[i][ncol-1] < target :
            i += 1
            
        curr_row = i
        if curr_row == nrow:
            return False
        
        j = ncol-1
        while j>=0:
            if matrix[curr_row][j] == target:
                print("Found at: ", curr_row, j)
                return True
            j -= 1
        print("Not Found")
        return False
        
if __name__ == '__main__':
    sol = Solution()
    
    # matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target1 = 13
    
    matrix2 = [[1]]
    target2 = 1
    print(sol.searchMatrix(matrix2, target2))