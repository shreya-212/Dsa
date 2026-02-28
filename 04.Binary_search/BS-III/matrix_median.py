# Given a 2D array matrix that is row-wise sorted. The task is to find the median of the given matrix.

#Brute force solution  -Time complexity:O(n*m log(n*m))  ,space complexity:O(n*m)
class Solution:
    def findMedian(self, matrix):
        new=[]
        for row in matrix:
            for val in row:
                new.append(val)
        new.sort()
        return new[len(new)//2]
    




#Optimal solution  -Time complexity:O(n*log m*log(max-min)) space complexity:O(1)
class Solution:
    def findMedian(self, matrix):
        n,m=len(matrix),len(matrix[0])
        def countLessEqual(row,target):
            left,right=0,len(row)
            while left<right:
                mid=(left+right)//2
                if row[mid]<=target:
                    left=mid+1
                else:
                    right=mid
            return left
        
        low=min(row[0] for row in matrix)
        high=max(row[-1] for row in matrix)
        required=(n*m)//2
        while low<=high:
            mid=(low+high)//2
            count=0
            for row in matrix:
                count+=countLessEqual(row,mid)
            if count<=required:
                low=mid+1
            else:
                high=mid-1
        return low

        

