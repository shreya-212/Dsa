# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.


#Brute Force Solution -Time complexity:O(n^3) ,space complexity:O(1)
class Solution:
    def subarraySum(self, nums, k):
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(i,n):
                sub_sum=0
                for x in range(i,j+1):
                    sub_sum+=nums[x]
                if sub_sum==k:
                    count+=1
        return count






#Better Solution -Time complexity:O(n^2),space complexity:O(1)
class Solution:
    def subarraySum(self, nums, k):
        count=0
        for i in range(len(nums)):
            sub_sum=0
            for j in range(i,len(nums)):
                sub_sum+=nums[j]
                if sub_sum==k:
                    count+=1
        return count






#Optimal SOlution -Time complexity:O(n), space complexity:O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        prefix=0
        prefix_count={0:1}
        count=0
        for num in nums:
            prefix+=num
            if prefix-k in prefix_count:
                count+=prefix_count[prefix-k]
            if prefix in prefix_count:
                prefix_count[prefix]+=1
            else:
                prefix_count[prefix]=1
        return count