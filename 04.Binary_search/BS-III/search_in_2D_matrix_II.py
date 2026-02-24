# Given a 2D array matrix where each row is sorted in ascending order from left to right and each column is sorted in 
# ascending order from top to bottom, write an efficient algorithm to search for a specific integer target in the matrix.

#Brute force solution  -Time complexity:O(m*n)  ,space complexity:O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        m,n=len(matrix),len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==target:
                    return True
        return False
    




#Better solution  -Time complexity:O(n log m )  ,space complexity:O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n,m=len(matrix),len(matrix[0])
        for row in range(n):
            if matrix[row][0]<=target<=matrix[row][m-1]:
                low,high=0,m-1
                while low<=high:
                    mid=(low+high)//2
                    if matrix[row][mid]==target:
                        return True
                    elif matrix[row][mid]<target:
                        low=mid+1
                    else:
                        high=mid-1
        return False
        



#Optimal solution  -Time complexity:O(n+m), space complexity:O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n,m=len(matrix),len(matrix[0])
        row=0
        col=m-1
        while row<n and col>=0:
            current=matrix[row][col]
            if current==target:
                return True
            elif current<target:
                row+=1
            else:
                col-=1
        return False