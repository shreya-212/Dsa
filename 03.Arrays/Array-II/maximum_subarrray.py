# Given an integer array nums, find the subarray with the largest sum, and return its sum.

#Brute Force Solution -Time complexity:O(n^2),space complexity:O(1)
class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        max_sum=float('-inf')
        for i in range(n):
            cur_sum=0
            for j in range(i,n):
                cur_sum+=nums[j]
                max_sum=max(cur_sum,max_sum)
        return max_sum




    

#Optimal Solution -Time Complexity:O(n),space complexity:O(1)
class Solution(object):
    def maxSubArray(self, nums):
        max_sum=float('-inf')
        cur_sum=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if cur_sum>max_sum:
                max_sum=cur_sum
            if cur_sum<0:
                cur_sum=0
        return max_sum

