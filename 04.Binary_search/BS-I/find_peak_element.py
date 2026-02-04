# Given an array arr of integers of size n. A peak element is defined as an element greater than both of its neighbors.



#Brute force solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution:
    def findPeakElement(self, arr):
        n=len(arr)
        if n==1:
            return 0
        for i in range(n):
            if i==0:
                if arr[i]>arr[i+1]:
                    return i
            elif i==n-1:
                if arr[i]>arr[i-1]:
                    return i
            else:
                if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    return i
        return -1







#Optimal solution  -Time complexity:O(log n)  ,space complexity:O(1)
class Solution(object):
    def findPeakElement(self, nums):
        low,high=0,len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1]:
                high=mid
            else:
                low=mid+1
        return low
