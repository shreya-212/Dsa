# Given a binary array nums, return the maximum number of consecutive 1's in the array.

#Brute force solution- Time complexity:O(n^2), space complexity:O(1)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        max_count=0
        for i in range(n):
            count=0
            for j in range(i,n):
                if nums[j]==1:
                    count+=1
                    max_count=max(max_count,count)
                else:
                    break
        return max_count







#Optimal Solution - Time complexity: O(n) ,space complexity: O(1)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        count=0
        max_count=0
        for i in range(n):
            if nums[i]==1:
                count+=1
            else:
                count=0
            if count>max_count:
                max_count=count
        return max_count
