'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
'''
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                isCol = True

            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(C):
                matrix[0][i] = 0

        if isCol:
            for i in range(R):
                matrix[i][0] = 0

matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]

matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [
    [1,2,3,4],
    [5,0,7,8],
    [0,10,11,12],
    [13,14,15,0]
]

print(matrix)
obj = Solution()
obj.setZeroes(matrix)
print(matrix)