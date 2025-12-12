# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.





#Brute Force Solution - Time complexity:O(n^2),space complexity:O(1)
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        for i in range(n):
            count=0
            for j in range(n):
                if nums[j]==nums[i]:
                    count+=1
            if count>(n//2):
                return nums[i]
        return -1
    




#Better Solution -Time complexity:O(n),space complexity:O(n)
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        for num,count in seen.items():
            if count>(n//2):
                return num
        return -1
            




#Optimal Solution - Time complexity:O(n),space complexity:O(1)
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        count=0
        element=0
        for num in nums:
            if count==0:
                count=1
                element=num
            elif element==num:
                count+=1
            else:
                count-=1
        if nums.count(element)>(n//2):
            return element
        return -1 
