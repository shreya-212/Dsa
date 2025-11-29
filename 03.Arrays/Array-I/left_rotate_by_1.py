# Given an integer array nums, rotate the array to the left by one.

#Brute Force Solution - Time Complexity: O(n), space complexity:O(n)

class Solution:
    def rotateArrayByOne(self, nums):
        n=len(nums)
        new=[0]*n
        for i in range(1,n):
            new[i-1]=nums[i]
        new[n-1]=nums[0]
        return new




#Optimal Solution -Time complexity :O(n),space complexity: O(1)
class Solution:
    def rotateArrayByOne(self, nums):
        if not nums:
            return
        first=nums[0]
        for i in range(1,len(nums)):
            nums[i-1]=nums[i]
        nums[-1]=first
        return nums
    

