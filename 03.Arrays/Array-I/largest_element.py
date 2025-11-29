# Given an array of integers nums, return the value of the largest element in the array

# Brute force solution-  Time complexity: O(n^2) ,Space complexity: O(1)
class Solution:
    def largestElement(self,nums):
        for i in range(len(nums)):
            large=True
            for j in range(len(nums)):
                if nums[j]>nums[i]:
                    large=False
                    break
            if large:
                return nums[i]



# Better solution- Time complexity: O(n log n),space Complexity:O(1)
class Solution:
    def largestElement(self, nums):
        nums.sort()
        return nums[-1]




#Optimal Solution -Time complexity: O(n), space complexity:O(1)
class Solution:
    def largestElement(self, nums):
        largest=nums[0]
        for n in nums:
            if n>largest:
                largest=n
        return largest

        