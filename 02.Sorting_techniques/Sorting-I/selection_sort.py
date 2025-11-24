# Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and 
# return the sorted array.

class Solution:
    def selectionSort( nums):
        n=len(nums)
        for i in range(0,n-1):
            curr_min=i
            for j in range(i+1,n):
                if nums[j]<nums[curr_min]:
                    curr_min=j
            nums[i],nums[curr_min]=nums[curr_min],nums[i]
        return nums
