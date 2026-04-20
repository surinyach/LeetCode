from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLUMNS = len(board), len(board[0])
        board_copy = [[0] * COLUMNS for _ in range(ROWS)]
        
        for i in range(ROWS):
            for j in range(COLUMNS):
                live = False
                if board[i][j]:
                    live = True

                # Vertical
                if i >= 1:
                    board_copy[i][j] += board[i-1][j]
                if i < ROWS - 1:
                    board_copy[i][j] += board[i+1][j]
                
                # Horizontal
                if j >= 1:
                    board_copy[i][j] += board[i][j-1]
                if j < COLUMNS - 1:
                    board_copy[i][j] += board[i][j+1]
                
                # Diagonal
                if j >= 1 and i >= 1:
                    board_copy[i][j] += board[i-1][j-1]
                if i < ROWS - 1 and j >= 1:
                    board_copy[i][j] += board[i+1][j-1]
                if i >= 1 and j < COLUMNS - 1:
                    board_copy[i][j] += board[i-1][j+1]
                if i < ROWS - 1 and j < COLUMNS - 1:
                    board_copy[i][j] += board[i+1][j+1]

                if i == 1 and j == 0:
                    print(board_copy[i][j])

                # Cell alive in next round or not
                if board_copy[i][j] == 3 and not live:
                    board_copy[i][j] = 1
                elif board_copy[i][j] > 1 and board_copy[i][j] < 4 and live:
                    board_copy[i][j] = 1
                else:
                    board_copy[i][j] = 0

        for i in range(ROWS):
            for j in range(COLUMNS):
                board[i][j] = board_copy[i][j]
        
        # Time Complexity: 2 * m * n -> O(m * n)
        # Space Complexity: Copy of board = m * n -> O(m * n) 