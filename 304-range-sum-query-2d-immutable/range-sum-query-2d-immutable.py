class NumMatrix(object):

    def __init__(self, matrix):
        ROW, COL = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(COL+1) for i in range (ROW+1)]

        for r in range(ROW):
            prefix = 0
            for c in range(COL):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix + above

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        topleft = self.sumMat[row1-1][col1-1]
        bottemright = self.sumMat[row2][col2]
        left = self.sumMat[row2][col1-1]
        above = self.sumMat[row1-1][col2]

        return bottemright + topleft - left - above

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)