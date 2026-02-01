# Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. 
# The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k 
# is not present return -1.


#Time complexity :O(log n)  ,space complexity;O(1)

class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1

                
     
