from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        zero_first_row = 1

        # determine which rows/cols need to be zero
        for i in range(ROWS):
            for j in range(COLUMNS):
                if matrix[i][j] == 0:
                    # Mark the row to be setted to 0
                    if i == 0:
                        zero_first_row = 0
                    else:
                        matrix[i][0] = 0

                    # Mark the columnto be setted to 0    
                    matrix[0][j] = 0
        
        # Set the marked rows and columns to 0
        # Skipping the first row and column since are the markers
        for i in range(1, ROWS):
            for j in range(1, COLUMNS):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle the first column and row:
        if matrix[0][0] == 0:
            for i in range(ROWS):
                matrix[i][0] = 0

        if zero_first_row == 0:
            for j in range(COLUMNS):
                matrix[0][j] = 0

        # Time Complexity: O(n^2)
        # Space Complexity: O(1)