# Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and
# return the sorted array

class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
