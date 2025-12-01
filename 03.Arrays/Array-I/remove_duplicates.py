# Given an integer array nums sorted in non-decreasing order,remove the duplicates in-place such that each unique element
# appears only once. The relative order of the elements should be kept the same

#Brute Force Solution - Time complexity:O(n), space complexity:O(n)
class Solution(object):
    def removeDuplicates(self, nums):
        seen=set()
        res=[]
        for n in nums:
            if n not in seen:
                seen.add(n)
                res.append(n)
        return res
    

    
#Optimal Solution - Time complexity:O(n), space complexity:O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        if not nums:
            return 0
        unique=0
        for j in range(1,n):
            if nums[j]!=nums[unique]:
                unique+=1
                nums[unique]=nums[j]
        return unique+1

