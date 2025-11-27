# Given an array of integers nums, return the second-largest element in the array. 
# If the second-largest element does not exist, return -1.

class Solution:
    def secondLargestElement(self, nums):
        first=second=float('-inf')
        for num in nums:
            if num>first:
                second,first=first,num
            elif num>second and num!=first:
                second=num
        if second==float('-inf'):
            return -1
        return second
    

