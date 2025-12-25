# Given an m x n matrix, return all elements of the matrix in spiral order.


#Time complexity: O(m*n), space complexity:O(1)

class Solution(object):
    def spiralOrder(self, matrix):
        res=[]
        if not matrix:
            return res
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while top<=bottom and left<=right:
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top+=1
            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right-=1
            if top<=bottom:
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                bottom-=1
            if left<=right:
                for row in range(bottom,top-1,-1):
                    res.append(matrix[row][left])
                left+=1
        return res


        
        