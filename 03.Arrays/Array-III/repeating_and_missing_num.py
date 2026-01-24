# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, 
# except for A, which appears twice and B which is missing.
# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index



#Brute force solution  -Time complexity:O(n^2) ,space complexity:O(1)
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        repeat=-1
        miss=-1
        for i in range(1,len(nums)+1):
            count=0
            for j in range(len(nums)):
                if nums[j]==i:
                    count+=1
            if count==2:
                repeat=i
            elif count==0:
                miss=i
            if repeat!=-1 and miss!=-1:
                    break
        return [repeat,miss]
    











#Better Solution  -Time complexity:O(n)  ,space complexity:O(n)
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        repeat=-1
        miss=-1
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for i in range(1,len(nums)+1):
            if i not in freq:
                miss=i
            elif freq[i]==2:
                repeat=i
        return [repeat,miss]

    










#Optimal Solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n=len(nums)
        sum_all=sum(nums)
        sum_sqr=sum(x*x for x in nums)

        expected_sum=n*(n+1)//2
        expected_sqr=n*(n+1)*(2*n+1)//6

        diff=sum_all-expected_sum
        sumRM=(sum_sqr-expected_sqr)//diff

        repeat=(diff+sumRM)//2
        miss=repeat-diff
        return [repeat,miss]



