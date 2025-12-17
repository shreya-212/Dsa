# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.



#Brute force solution -Time complexity:O(n*m) ,space compelexity:O(n+m)
class Solution:
    def setZeroes(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        row_0=set()
        col_0=set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_0.add(i)
                    col_0.add(j)
        for i in range(row):
            for j in range(col):
                if i in row_0 or j in col_0:
                    matrix[i][j]=0




#Optimal Solution -Time complexity:O(n*m) ,space complexity:O(1)
class Solution(object):
    def setZeroes(self, matrix):
        row=len(matrix)
        col=len(matrix[0])
        first_row_0=False
        first_col_0=False
        for j in range(col):
            if matrix[0][j]==0:
                first_row_0=True
                break
        for i in range(row):
            if matrix[i][0]==0:
                first_col_0=True
                break
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if first_row_0:
            for j in range(col):
                matrix[0][j]=0
        if first_col_0:
            for i in range(row):
                matrix[i][0]=0

            
            
            