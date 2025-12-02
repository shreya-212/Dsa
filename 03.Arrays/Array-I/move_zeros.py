# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Brute force Solution- Time complexity: O(n^2), space complexity: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        i=0
        while i<n:
            if nums[i] ==0:
                for j in range(i+1,n):
                    nums[j-1]=nums[j]
                nums[n-1]=0
                n-=1      
            else:
                i+=1
        return nums


#Better solution - Time complexity: O(n),space complexity: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        i=0
        for j in range(n):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
        for j in range(i,n):
            nums[j]=0
        return nums





#Optimal Solution- Time complexity: O(n), space complexity: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                if i!=j:
                    nums[i],nums[j]=nums[j],nums[i]
                i+=1
        return nums