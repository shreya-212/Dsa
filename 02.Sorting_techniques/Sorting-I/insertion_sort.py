# Given an array of integers called nums, sort the array in non-decreasing order 
# using the insertion sort algorithm and return the sorted array.

class Solution:
    def insertionSort(self, nums):
        n=len(nums)
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums
