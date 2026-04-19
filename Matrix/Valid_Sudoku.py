class Solution(object):
    def check(self, ini_row, end_row, ini_col, end_col, board):
        numbers = [0] * 9
        for i in range(ini_row, end_row):
            for j in range(ini_col, end_col):
                num = ord(board[i][j]) - 48 - 1
                if num >= 0 and num <= 8:
                    if numbers[num] != 0:
                        return False
                    else:
                        numbers[num] = 1
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        valid = True
        # Check rows
        for i in range(0, len(board)):
            valid = self.check(i, i + 1, 0, len(board), board)
            if not valid:
                return False

        # Check columns
        for j in range (0, len(board)):
            valid = self.check(0, len(board), j, j + 1, board)
            if not valid:
                return False

        # Check sub-boxes
        row = 0
        col = 0 
        while row <= 6:
            valid = self.check(row, row + 3, col, col + 3, board)
            if not valid:
                return False
            col += 3
            if col > 6:
                row += 3
                col = 0
        
        return valid