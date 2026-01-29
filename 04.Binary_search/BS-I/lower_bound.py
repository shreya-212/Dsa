# Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
# The lower bound algorithm finds the first and smallest index in a sorted array where the value at that 
# index is greater than or equal to a given key i.e. x.


#Brute force solution   -Time complexity:O(n)  ,space complexity:O(1)
class Solution:
    def lowerBound(self, nums, x):
        for i in range(len(nums)):
            if nums[i]>=x:
                return i
        return len(nums)







#Optimal solution  -Time complexity:O(log n)   ,space complexity:O(1)
class Solution:
    def lowerBound(self, nums, x):
        low,high=0,len(nums)-1
        ans=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
