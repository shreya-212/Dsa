# Given an array of integers called nums, sort the array in non-decreasing order using the quick sort algorithm 
# and return the sorted array.


class Solution:
    def quickSort(self, nums,low=None,high=None):
        if low==None and high==None:
            low,high=0,len(nums)-1
            self.quickSort(nums,low,high)
            return nums
        if low<high:
            p=self.partition(nums,low,high)
            self.quickSort(nums,low,p-1)
            self.quickSort(nums,p+1,high)
    def partition(self,nums,low,high):
        pivot =nums[high]
        i=low-1
        for j in range(low,high):
            if nums[j]<=pivot:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        nums[i+1],nums[high]=nums[high],nums[i+1]
        return i+1

        