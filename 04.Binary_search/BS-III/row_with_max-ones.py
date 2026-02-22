# Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order,
# find the index of the row with the maximum number of ones.


#Brute force solution   -Time complexity:O(n*m) ,space complexity:O(1)
class Solution:
    def rowWithMax1s(self, mat):
        if not mat:
            return -1
        indx=-1
        cnt_max=0
        row,col=len(mat),len(mat[0])
        for r in range(row):
            count=0
            for c in range(col):
                if mat[r][c]==1:
                    count+=1
            if count>cnt_max:
                cnt_max=count
                indx=r
        return indx

        
#Better solution  -Time complexity:O(n log m)   ,space complexity:O(1)
class Solution:
    def rowWithMax1s(self, mat):
        if not mat:
            return -1
        n,m=len(mat),len(mat[0])
        cnt_max=0
        ans=-1
        for r in range(n):
            low,high=0,m-1
            first_1=-1
            while low<=high:
                mid=(low+high)//2
                if mat[r][mid]==1:
                    first_1=mid
                    high=mid-1
                else:
                    low=mid+1
            if first_1 != -1:
                count=m-first_1
                if count>cnt_max:
                    cnt_max=count
                    ans=r
        return ans



        
#Optimal solution  -Time complexity:O(n+m)  ,space complexity:O(1)
class Solution:
    def rowWithMax1s(self, mat):
        if not mat:
            return -1
        n,m=len(mat),len(mat[0])
        row=0
        col=m-1
        ans=-1
        while row<n and col>=0:
            if mat[row][col]==1:
                ans=row
                col-=1
            else:
                row+=1
        return ans




        
        
         
       
        
       