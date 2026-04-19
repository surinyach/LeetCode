class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = 0
        c = 0

        min_row = 1
        min_col = 0
        max_row = len(matrix) - 1
        max_col = len(matrix[0]) - 1

        directions = ["right", "down", "left", "up"]

        solution = []
        d = directions[0]
        while len(solution) < len(matrix) * len(matrix[0]):
            # Right Movement
            if d == "right":
                if c <= max_col:
                    solution.append(matrix[r][c])
                    c += 1
                else:
                    c -= 1
                    r += 1
                    max_col -= 1
                    d = directions[1]
            
            # Down Movement
            if d == "down":
                if r <= max_row:
                    solution.append(matrix[r][c])
                    r += 1
                else:
                    r -= 1
                    c -= 1
                    max_row -= 1
                    d = directions[2]

            # Left Movement
            if d == "left":
                if c >= min_col:
                    solution.append(matrix[r][c])
                    c -= 1
                else:
                    c += 1
                    r -= 1
                    min_col += 1
                    d = directions[3]
            
            # Up Movement
            if d == "up":
                if r >= min_row:
                    solution.append(matrix[r][c])
                    r -= 1
                else:
                    c += 1
                    r += 1
                    min_row += 1
                    d = directions[0]
                
        return solution