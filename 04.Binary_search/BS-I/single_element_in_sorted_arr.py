# Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice. 
# Find the single number in the array.


#Brute force solution  -Time complexity:O(n) , space complexity:O(1)
class Solution(object):
    def singleNonDuplicate(self, nums):
        result=0
        for num in nums:
            result^=num
        return result
           

           




#Optimal solution   -Time complexity:O(log n), space complexity:O(1)
class Solution(object):
    def singleNonDuplicate(self, nums):
        low,high=0,len(nums)-1
        while low<high:
            mid=(low+high)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                low=mid+2
            else:
                high=mid
        return nums[low]
           




        