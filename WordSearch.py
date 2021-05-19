'''
https://leetcode.com/problems/word-search
'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        EDGES = [(0,1), (1,0), (0, -1), (-1, 0)]
        
        def backtrack(row, col, suffix):
            if not suffix:
                return True

            if not 0 <= row < row_length or \
                not 0 <= col < col_length or \
                suffix[0] != board[row][col]:
                return False

            board[row][col] = '#'

            for edge in EDGES:
                if backtrack(row + edge[0], col + edge[1], suffix[1:]):
                    return True

            board[row][col] = suffix[0]
            
            return False


        row_length = len(board)
        col_length = len(board[0])

        for i in range(row_length):
            for j in range(col_length):
                if backtrack(i, j, word):
                    return True

        return False

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = 'ABCCED'
word = 'ABCB'
obj = Solution()
print(obj.exist(board, word))