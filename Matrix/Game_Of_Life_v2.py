from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLUMNS = len(board), len(board[0])
        neighbours = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [1,-1], [-1, 1]]

        # Truth Table:
        # Original Value - New Value -> Assigned Number
        # 0 - 0 -> 0 
        # 1 - 0 -> 1  
        # 0 - 1 -> 2  
        # 1 - 1 -> 3

        for i in range(ROWS):
            for j in range(COLUMNS):
                alive_neighbours = 0

                # Check neighbour state
                for n in neighbours:
                    n_row = i + n[0]
                    n_col = j + n[1]
                    if n_row >= 0 and n_row <= ROWS - 1 and n_col >= 0 and n_col <= COLUMNS - 1:
                        if board[n_row][n_col] == 1 or board[n_row][n_col] == 3:
                            alive_neighbours += 1

                # Update cell state        
                if board[i][j] == 1:
                    if alive_neighbours == 2 or alive_neighbours == 3:
                        board[i][j] = 3
                else:
                    if alive_neighbours == 3:
                        board[i][j] = 2
                
        # Update the state based on the table of truth
        for i in range(ROWS):
            for j in range(COLUMNS):
                if board[i][j] == 1:
                    board[i][j] = 0

                elif board[i][j] > 1:
                    board[i][j] = 1

    # Time Complexity: O(m*n)
    # Space Complexity: O(1)