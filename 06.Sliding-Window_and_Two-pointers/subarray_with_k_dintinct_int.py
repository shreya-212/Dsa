# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.




#Brute force solution  -Time complexity:O(n^2)  ,space cmplexity:O(n)
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        count=0
        for i in range(len(nums)):
            check=set()
            for j in range(i,len(nums)):
                check.add(nums[j])
                if len(check)==k:
                    count+=1
                elif len(check)>k:
                    break
        return count
        



#Optimal solution  -Time complexity:O(n)  ,space complexity:O(n)
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atmost(nums,k):
            count=0
            freq={}
            left=0
            for right in range(len(nums)):
                freq[nums[right]]=freq.get(nums[right],0)+1
                while len(freq)>k:
                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left+=1
                count+=right-left+1
            return count
        return atmost(nums,k)-atmost(nums,k-1)