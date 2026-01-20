# Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.



#Brute force solution -Time complexity:O(n^2) ,space complexity:O(1)
class Solution:
    def subarraysWithXorK(self, nums, k):
        n=len(nums)
        count=0
        for i in range(n):
            result=0
            for j in range(i,n):
                result^=nums[j]
                if result==k:
                    count+=1
        return count
    





#Optimal solution  -Time complexity:O(n)  ,space complexity:O(n)
class Solution:
    def subarraysWithXorK(self, nums, k):
        prefix={0:1}
        xor_val=0
        count=0
        for num in nums:
            xor_val^=num
            count+=prefix.get(xor_val^k,0)
            prefix[xor_val]=prefix.get(xor_val,0)+1
        return count
