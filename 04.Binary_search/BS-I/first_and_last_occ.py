# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a 
# given target value.If target is not found in the array, return [-1, -1].



#Brute force solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def searchRange(self, nums, target):
        n=len(nums)
        first=last=-1
        for i in range(n):
            if nums[i]==target:
                if first==-1:
                    first=i
                last=i
        return [first,last]
    



#Optimal solution  -Time complexity:O(log n)  ,space complexity:O(1)
class Solution(object):
    def searchRange(self, nums, target):
        def first_occ(nums,target):
            low,high=0,len(nums)-1
            first=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    first=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return first

        def last_occ(nums,target):
            low,high=0,len(nums)-1
            last=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    last=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return last
        return [first_occ(nums,target), last_occ(nums,target)]
        



              
            

        