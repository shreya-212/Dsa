# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.


#Brute force Solution -Time complexity:O(n^2), space complexity:O(1)
class Solution(object):
    def singleNumber(self, nums):
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count==1:
                return nums[i]
                





#better solution - Time complexity:O(n),space complexity:O(n)
class Solution(object):
    def singleNumber(self, nums):
        check={}
        for i in nums:
            check[i]=check.get(i,0)+1
        for i in nums:
            if check[i]==1:
                return i
            





#Optimal Solution -Timec complexity:O(n) ,space complexity:O(1)
class Solution(object):
    def singleNumber(self, nums):
        result=0
        for n in nums:
            result^=n
        return result