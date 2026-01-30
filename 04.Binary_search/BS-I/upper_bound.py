# Given a sorted array of nums and an integer x, write a program to find the upper bound of x.
# The upper bound of x is defined as the smallest index i such that nums[i] > x.





#Brute force solution  -Time complexity:O(n)  , space complexity:O(1)
class Solution:
    def upperBound(self, nums, x):
        for i in range(len(nums)):
            if nums[i]>x:
                return i
        return len(nums)






#Optimal Solution  -Time complexity:O(log n) , space complexity:O(1)
class Solution:
    def upperBound(self, nums, x):
        low,high=0,len(nums)-1
        ans=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans