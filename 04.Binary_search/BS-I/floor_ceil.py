# Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element 
# in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than 
# or equal to x. If no floor or ceil exists, output -1.





class Solution:
    def getFloorAndCeil(self, nums, x):
        low,high=0,len(nums)-1
        floor=ceil=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==x:
                return nums[mid],nums[mid]
            elif nums[mid]<x:
                floor=nums[mid]
                low=mid+1
            else:
                ceil=nums[mid]
                high=mid-1
        return floor,ceil
               
        
       
