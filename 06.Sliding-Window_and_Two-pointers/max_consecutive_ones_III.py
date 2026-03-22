# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


#Brute force solution  -Time complexity:O(n^2)  ,Space complexity:O(1)
class Solution(object):
    def longestOnes(self, nums, k):
        max_len=0
        for i in range(len(nums)):
            count_0=0
            for j in range(i,len(nums)):
                if nums[j]==0:
                    count_0+=1
                if count_0>k:
                    break
                max_len=max(max_len,j-i+1)
        return max_len
    





#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def longestOnes(self, nums, k):
        max_len=0
        left=0
        zero=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
          
            while zero>k:
                if nums[left]==0:
                    zero-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len