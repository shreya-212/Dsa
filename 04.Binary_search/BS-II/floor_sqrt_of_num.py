# Given a positive integer n. Find and return its square root. If n is not a perfect square, 
# then return the floor value of sqrt(n).




#Brute force solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution:
    def floorSqrt(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            if i*i<=n:
                ans=i
            else:
                break
        return ans





#Optimal solution  -Time complexity:O(log n)  ,space complexity:O(1)
class Solution:
    def floorSqrt(self, n: int) -> int:
        low,high=0,n
        ans=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans

