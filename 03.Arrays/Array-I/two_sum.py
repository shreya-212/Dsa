# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


#Brute force Solution- Time complexity:O(n),space complexity:O(1)
class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]


#Better Solution-Time complexity:O(n log n),space complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        arr=[(num,i) for i,num in enumerate(nums)]
        arr.sort()
        left,right=0,len(arr)-1
        while left<right:
            s=arr[left][0]+arr[right][0]
            if s==target:
                return [arr[left][1],arr[right][1]]
            if s<target:
                left+=1
            else:
                right-=1







#Optimal Solution- Time complexity:O(n), space complexity:O(n)
class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        seen={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i
