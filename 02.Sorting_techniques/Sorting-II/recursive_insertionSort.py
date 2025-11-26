# Given an array of integers nums, sort the array in non-decreasing order using the recursive Insertion Sort algorithm, 
# and return the sorted array.

class Solution:
    def insertionSort(self, nums,n=None):
        if n is None:
            n=len(nums)
        if n<=1:
            return 
        self.insertionSort(nums,n-1)
        key=nums[n-1]
        j=n-2
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
        return nums
        
