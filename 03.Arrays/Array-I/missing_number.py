# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), 
# return the only number missing from the array within this range.



#Brute force solution- Time complexity:O(n^2) ,space complexity:O(1)
class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
            


            

#Better Solution -Time complexity:O(n),space complexity:O(1)

class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        return n*(n+1)//2-sum(nums)
            
            
            

#Optimal Solution - Time complexity:O(n), space complexity:O(1)

class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        i=0
        while i<n:
            index=nums[i]
            if index<n and nums[i]!=nums[index]:
                nums[i],nums[index]=nums[index],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i:
                return i
        return n