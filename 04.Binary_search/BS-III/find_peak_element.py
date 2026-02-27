# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left,
# right, top, and bottom. Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] 
# and return the length 2 array [i,j].


#Brute force solution  -Time complexity:O(m*n)  ,space complexity:O(1)
class Solution(object):
    def findPeakGrid(self, mat):
        n,m=len(mat),len(mat[0])
        for i in range(n):
            for j in range(m):
                current=mat[i][j]
                peak=True
                if i>0 and mat[i-1][j]>=current:
                    peak=False
                if i<n-1 and mat[i+1][j]>=current:
                    peak=False
                if j>0 and mat[i][j-1]>=current:
                    peak=False
                if j<m-1 and mat[i][j+1]>=current:
                    peak=False
                if peak:
                    return [i,j]
                




#Optimal solution  -Time complexity:O(n log m)  ,space complexity:O(1)
class Solution(object):
    def findPeakGrid(self, mat):
        n,m=len(mat),len(mat[0])
        low,high=0,m-1
        while low<=high:
            mid=(low+high)//2
            max_row=0
            for row in range(n):
                if mat[row][mid]>mat[max_row][mid]:
                    max_row=row
            left=mat[max_row][mid-1] if mid>0 else -1
            right=mat[max_row][mid+1] if mid<m-1 else -1
            if mat[max_row][mid]>left and mat[max_row][mid]>right:
                return [max_row,mid]
            elif left>mat[max_row][mid]:
                high=mid-1
            else:
                low=mid+1
                    


        
        