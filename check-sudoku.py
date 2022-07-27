# https://leetcode.com/problems/valid-sudoku/

class Solution:

    def isValidList(self, section):
        pruned = []
        for element in section:
            if element != ".":
                if int(element) > 9 or int(element) < 0:
                    return False
                else:
                    pruned.append(int(element))
        return len(pruned) == len(set(pruned))
        
    def isValidSudoku(self, board):
        isValid = True
        
        for row in board:
            if not self.isValidList(row):
                isValid = False
                break
        
        columns = [[board[i][j] for i in range(9)] for j in range(9)]

        for col in columns:
            if not self.isValidList(col):
                isValid = False
                break
        
        squares = [[board[3*(sel//3) + i][3*(sel%3) + j] for i in range(3)  for j in range(3) ]for sel in range(9)]

        for square in squares:
            if not self.isValidList(square):
                isValid = False
                break
        
        return isValid

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]

result = sol.isValidSudoku(board)

print(result)