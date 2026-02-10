# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.



#   Time complexity:O(n)  , space complexity:O(1)
class Solution(object):
    def findKthPositive(self, arr, k):
        miss=k
        for num in arr:
            if num<=miss:
                miss+=1
            else:
                break
        return miss
        






#Optimal solution    -Time complexity:O(log n) ,space complexity:O(1)
class Solution(object):
    def findKthPositive(self, arr, k):
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            missing=arr[mid]-(mid+1)
            if missing<k:
                low=mid+1
            else:
                high=mid-1
        return high+1+k
