# Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, and the first element of a row is
# greater than the last element of the previous row (if it exists), and an integer target, determine if 
# the target exists in the given mat or not.


#Brute force solution  -Time complexity:O(m*n)  ,space complexity:O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        m,n=len(matrix),len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==target:
                    return True
        return False
        




#Better solution  -Time complexity:O(n log m)  ,space complexity:O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
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







#Optimal solution  -Time complexity:O(log(n*m))  space complexity:O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        n,m=len(matrix),len(matrix[0])
        low,high=0,n*m-1
        while low<=high:
            mid=(low+high)//2
            row=mid//m
            col=mid%m
            num=matrix[row][col]
            if num==target:
                return True
            elif num<target:
                low=mid+1
            else:
                high=mid-1
        return False
