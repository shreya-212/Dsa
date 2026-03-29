# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.




#Brute force solution  -Time complexity:O(n^2)  ,space omplexity:O(1)
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        nice=0
        for i in range(len(nums)):
            count=0
            for j in range(i,len(nums)):
                if nums[j]%2==1:
                    count+=1
                if count==k:
                    nice+=1
        return nice
                



#Better solution  -Time complexity:O(n) ,space complexity:O(n)
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count=0
        freq={0:1}
        nice=0
        for num in nums:
            if num %2==1:
                count+=1
           
            nice+=freq.get(count-k,0)
            freq[count]=freq.get(count,0)+1
        return nice
    



#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def atmost(nums,k):
            count=0
            nice=0
            left=0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    count+=1
                while count>k:
                    if nums[left]%2==1:
                        count-=1
                    left+=1
                nice+=right-left+1
            return nice
        return atmost(nums,k)-atmost(nums,k-1)
