# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.




# Time complexity :O(log n)  ,space complexity:O(1)
class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid =(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1

        

        