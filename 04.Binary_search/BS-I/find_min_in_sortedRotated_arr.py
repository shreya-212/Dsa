# Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown number 
# of times (between 1 and N), find the minimum element in the array.



# Brute force solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def findMin(self, nums):
        min_val=float('inf')
        for num in nums:
            if num<min_val:
                min_val=num
        return min_val




#Optimal Solution   -Time complexity:O(log n)  ,space complexity:O(1)
class Solution(object):
    def findMin(self, nums):
        low,high=0,len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>=nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]