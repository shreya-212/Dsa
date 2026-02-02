# Given an integer array nums, sorted in ascending order (may contain duplicate values) and a target value k. 
# Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.



# Time complexity:O(log n)  ,space complexity:O(1)
class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            elif nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            
        return False