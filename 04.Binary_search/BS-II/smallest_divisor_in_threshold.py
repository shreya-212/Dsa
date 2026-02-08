# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all 
# the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is 
# less than or equal to threshold.


#Brute force solution  -Time complexity:O(n*max(nums))  ,space complexity:O(1)
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        for i in range(1,max(nums)+1):
            sum_all=0
            for j in range(len(nums)):
                sum_all+=(nums[j]+i-1)//i
            if sum_all<=threshold:
                return i





#Optimal solution    -Time complexity:O(n log(max(nums)))  ,space complexity:O(1)
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def count_sum(nums,d):
            sum_all=0
            for num in nums:
                sum_all+=(num+d-1)//d
            return sum_all
        low,high=1,max(nums)
        while low<high:
            mid=(low+high)//2
            sum_all=count_sum(nums,mid)
            if sum_all<=threshold:
                high=mid
            else:
                low=mid+1
        return low
