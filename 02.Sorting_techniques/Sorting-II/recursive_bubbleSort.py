# Given an array of integers nums, sort the array in non-decreasing order using the recursive Bubble Sort algorithm,
# and return the sorted array

class Solution:
    def bubbleSort(self, nums,n=None):
        if n is None:
            n=len(nums)
        if n==1:
            return nums
        for j in range(n-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        return self.bubbleSort(nums,n-1)

