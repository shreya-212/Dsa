# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false

#Brute Force Solution - Time complexity:O(n^2), Space complexity:O(1)

class Solution:
    def isSorted(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    return False
        return True
 




# Optimal Solution - Time complexity:O(n),Space complexity:O(1)

class Solution:
    def isSorted(self, nums):
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return False
        return True
    

    
    
