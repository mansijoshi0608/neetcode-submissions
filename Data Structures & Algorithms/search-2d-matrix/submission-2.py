class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)-1
        n=len(matrix[0])-1
        if target>matrix[m][n] or target<matrix[0][0]:
            return False
        row=0
        col=n
        while(row<=m and col>=0):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col=col-1
            else:
                row=row+1
        return False
        