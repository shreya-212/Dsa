# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray 
# is minimized. Return the minimized largest sum of the split.


#Brute force solution  -Time complexity:O(n*sum(nums))  ,space complexity:O(1)
class Solution(object):
    def splitArray(self, nums, k):
        def count_subsum(x):
            subcount=1
            subsum=0
            for num in nums:
                if subsum+num<=x:
                    subsum+=num
                else:
                    subcount+=1
                    subsum=num
            return subcount

        for x in range(max(nums),sum(nums)+1):
            subcount=count_subsum(x)
            if subcount<=k:
                return x




#Optimal solution    -Time complexity:O(n*log(sum(nums)))  ,space complexity:O(1)
class Solution(object):
    def splitArray(self, nums, k):
        def count_subsum(x):
            subcount=1
            subsum=0
            for num in nums:
                if subsum+num<=x:
                    subsum+=num
                else:
                    subcount+=1
                    subsum=num
            return subcount

        low,high=max(nums),sum(nums)
        while low<=high:
            mid=(low+high)//2
            subcount=count_subsum(mid)
            if subcount<=k:
                high=mid-1
            else:
                low=mid+1
        return low
