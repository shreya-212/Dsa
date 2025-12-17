# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#Brute force Solution -Time complexity: O(n^2),space complexity:O(n^2)
class Solution:
    def rotateMatrix(self, matrix):
        n=len(matrix)
        mat2=[[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                mat2[j][n-1-i]=matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j]=mat2[i][j]








#Optimal Solution -Time complexity: O(n^2),space complexity:O(1)
class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()