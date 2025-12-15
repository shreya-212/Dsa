# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#Brute force Solution -Time complexity:O(n^2),space complexity:O(1)
class Solution(object):
    def longestConsecutive(self, nums):
        max_len=0
        for num in nums:
            current=num
            length=1
            while current+1 in nums:
                length+=1
                current+=1
            max_len=max(max_len,length)
        return max_len





#Better solution -Time complexity:O(n log n), space complexity:O(1)
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        max_len=1
        cur_len=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                cur_len+=1
            else:
                cur_len=1
            max_len=max(max_len,cur_len)
        return max_len







#Optimal Solution -Time complexity:O(n),space complexity:O(n)
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        max_len=0
        seen=set(nums)
        for num in seen:
            if num-1 not in seen:
                cur_num=num
                length=1
                while cur_num+1  in seen:
                    cur_num+=1
                    length+=1
                max_len=max(max_len,length)
        return max_len

                
            