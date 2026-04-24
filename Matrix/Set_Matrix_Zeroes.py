class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols= set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if not i in zero_rows:
                        zero_rows.add(i)
                    if not j in zero_cols:
                        zero_cols.add(j)

        for r in zero_rows:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0

        for c in zero_cols:
            for i in range(len(matrix)):
                matrix[i][c] = 0

        # Time Complexity: O(n*m) -> Search the matrix searching for 0s
        # Space Complexity: O(n+m) -> If all the original matrix is filled with 0s, the sets will store all rows and cols indexes