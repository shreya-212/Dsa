# Given an array of integers nums, return the second-largest element in the array. 
# If the second-largest element does not exist, return -1.


#Brute Force Solution - Time complexity:O(n log n)  ,Space complexity:O(1)

class Solution:
    def secondLargestElement(self,nums):
        nums.sort()
        largest = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            if nums[i] != largest:
                return nums[i]
        return None
    


#Better Solution- Time complexity:O(n), Space complexity:O(1)  

class Solution:
    def secondLargestElement(self,nums):
        largest=nums[0]
        second=float('-inf')
        if len(nums)<2:
            return None
        for i in nums:
            if i>largest:
                largest=i
        for i in nums:
            if i>second and i!=largest:
                second=i
        if second==float('-inf'):
            return None
        return second
            



#Optimal Solution -Time complexity: O(n), space complexity:O(1)
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
    

