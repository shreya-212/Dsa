# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps



# Brute Force Solution- Time complexity: O(nk) ,space complexity: O(1)
class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n=len(nums)
        k%=n
        for i in range(k):
            first=nums[0]
            for j in range(1,n):
                nums[j-1]=nums[j]
            nums[n-1]=first
        return nums





#Better Solution- Time complexity:O(n) ,Space complexity: O(n)
class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n=len(nums)
        if n==0:
            return nums
        k%=n
        return nums[k:]+nums[:k]
    




#Optimal Solution- Time complexity:O(n), space complexity: O(1)
class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n=len(nums)
        if n==0:
            return nums
        k%=n
        def rev(start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        rev(0,k-1)
        rev(k,n-1)
        rev(0,n-1)
        return nums
