# You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.
# Return the count of occurrences of target in the array.

#Brute force solution  -Time complexity:O(n) ,space complexity:O(1)
class Solution:
    def countOccurrences(self, arr, target):
        count=0
        for num in arr:
            if num==target:
                count+=1
        return count
    





#Optimal solution  -Time complexity:O(log n)  ,space complexity:O(1)
class Solution:
    def countOccurrences(self, nums, target):

        def first_occ(nums,target):
            low,high=0,len(nums)-1
            first=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    first=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return first
        def last_occ(nums,target):
            low,high=0,len(nums)-1
            last=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    last=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return last
        first=first_occ(nums,target)
        last=last_occ(nums,target)
        if first==-1:
            return 0
        return last-first+1
