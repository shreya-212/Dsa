




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
        