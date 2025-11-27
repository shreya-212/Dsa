# Given an array of integers nums, return the value of the largest element in the array

class Solution:
    def largestElement(self, nums):
        largest=nums[0]
        for n in nums:
            if n>largest:
                largest=n
        return largest

        