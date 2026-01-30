# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, 
# return the index where it would be if it were inserted in order.




# Time complexity: O(log n) ,space complexity: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        low,high=0,len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                high=mid-1
            else:
                low=mid+1
        return low
       