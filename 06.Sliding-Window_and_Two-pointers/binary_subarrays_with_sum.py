# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.


#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(1)
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count=0
        for i in range(len(nums)):
            subsum=0
            for j in range(i,len(nums)):
                subsum+=nums[j]
                if subsum==goal:
                    count+=1
        return count
    




#Better solution  -Time complexity:O(n)  ,space complexity:O(n)
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix={0:1}
        subsum=0
        count=0
        for num in nums:
            subsum+=num
            if subsum-goal in prefix:
                count+=prefix[subsum-goal]
            prefix[subsum]=prefix.get(subsum,0)+1
        return count





#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def atmost(nums,goal):
            if goal<0:
                return 0
            count=0
            subsum=0
            left=0
            for right in range(len(nums)):
                subsum+=nums[right]
    
                while subsum>goal:
                    subsum-=nums[left]
                    left+=1
                count+=(right-left+1)
            return count
        return atmost(nums,goal)-atmost(nums,goal-1)
