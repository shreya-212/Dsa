# Given an array nums of size n and an integer k,find the length of the longest 
# sub-array that sums to k. If no such sub-array exists, return 0.


#Brute force - Time complexity:O(n^2),space complexity:O(1)
class Solution:
    def longestSubarray(self, nums, k):
        n=len(nums)
        max_count=0
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                if sum==k:
                    max_count=max(max_count,j-i+1)
        return max_count
    




#Better Solution - Time complexity:O(n),space complexity :O(n)
class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum=0
        occurance={0:-1}
        max_len=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]

            if (prefix_sum-k) in occurance:
                length=i-occurance[prefix_sum-k]
                if length>max_len:
                    max_len=length
            if prefix_sum not in occurance:
                occurance[prefix_sum]=i
        return max_len





#Optimal solution- Time complexity:O(n),space complexity:O(1)
class Solution:
    def longestSubarray(self, nums, k):
        n=len(nums)
        j=0
        current_sum=0
        max_len=0
        for i in range(n):
            current_sum+=nums[i]
            while current_sum>k and j<=i:
                current_sum-=nums[j]
                j+=1
            if current_sum==k:
                max_len=max(max_len,i-j+1)
        return max_len