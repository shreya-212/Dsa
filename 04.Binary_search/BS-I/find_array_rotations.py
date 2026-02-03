# Given an integer array nums of size n, sorted in ascending order with distinct values. 
# The array has been right rotated an unknown number of times, between 0 and n-1 (including). 
# Determine the number of rotations performed on the array.



#Brute force solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution:
    def findKRotation(self, nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i+1
        return 0




#Optimal solution  -Time complexity:O(log n)  ,space complexity:O(1)
class Solution:
    def findKRotation(self, nums):
        low,high=0,len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>=nums[high]:
                low=mid+1
            else:
                high=mid
        return low
