class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = {}
        for i in range(len(matrix)):
            rows[i] = []
            for j in range(len(matrix)):
                rows[i].append(matrix[i][j])
        
        index = len(matrix) - 1
        for j in range(len(matrix)):
            for i in range(len(matrix)):
                matrix[i][j] = rows[index][i]
            index -= 1

        # Time Complexity: 2n^2 -> O(n^2)
        # Space Complexity: O(n^2): rows stores all matrix elements