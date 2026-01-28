# Given an integer array nums. Find the subarray with the largest product, 
# and return the product of the elements present in that subarray.




#Brute force Solution  -Time complexity:O(n^2)  ,space complexity:O(1)
class Solution(object):
    def maxProduct(self, nums):
        n=len(nums)
        max_prod=float('-inf')
        for i in range(n):
            prod=1
            for j in range(i,n):
                prod*=nums[j]
                max_prod=max(max_prod,prod)
        return max_prod
    







#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def maxProduct(self, nums):
        n=len(nums)
        prefix=1
        suffix=1
        max_prod=float('-inf')
        for i in range(n):
            prefix*=nums[i]
            suffix*=nums[n-i-1]
            
            max_prod=max(max_prod,prefix,suffix)
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
        return max_prod
    







#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def maxProduct(self, nums):
        max_prod=nums[0]
        min_prod=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            cur=nums[i]
            if cur<0:
                max_prod,min_prod=min_prod,max_prod

            max_prod=max(cur,max_prod*cur)
            min_prod=min(cur,min_prod*cur)
            result=max(result,max_prod)
        return result