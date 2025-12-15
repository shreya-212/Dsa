# Given an integer array nums, return a list of all the leaders in the array.
# The rightmost element is always a leaderThe elements in the leader array must appear in the order they appear in the nums array.





#Brute force Solution -Time complexity:O(n^2),space complexity:O(1)
class Solution:
    def leaders(self, nums):
        result=[]
        for i in range(len(nums)):
            leader=True
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    leader=False
                    break
            if leader:
                result.append(nums[i])
        return result







#Optimal Solution -Time complexity:O(n),space complexity:O(n)
class Solution:
    def leaders(self, nums):
        if not nums:
            return []
        cur_max=float('-inf')
        result=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=cur_max:
                cur_max=nums[i]
                result.append(cur_max)
        return result[::-1]
            