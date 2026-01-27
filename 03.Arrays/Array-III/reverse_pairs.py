# Given an integer array nums. Return the number of reverse pairs in the array.
# An index pair (i, j) is called a reverse pair if: nums[i] > 2 * nums[j]




#Brute force Solution -Time complexity:O(n^2)  ,space complexity:O(1)
class Solution(object):
    def reversePairs(self, nums):
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]> ( 2* nums[j]):
                    count+=1
        return count











#Optimal Solution  -Time complexity:O(n log n)  ,space complexity:O(n)

class Solution:
    def reversePairs(self, nums):
        def merge_sort(low,high):
            if low>=high:
                return 0
            mid=(low+high)//2
            count=merge_sort(low,mid)+merge_sort(mid+1,high)
            count+=count_pairs(low,mid,high)
            merge(low,mid,high)
            return count
        
        def count_pairs(low,mid,high):
            count=0
            j=mid+1
            for i in range(low,mid+1):
                while j<=high and nums[i]>(2*nums[j]):
                    j+=1
                count+=(j-(mid+1))
            return count
        
        def merge(low,mid,high):
            merged=[]
            left,right=low,mid+1
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    merged.append(nums[left])
                    left+=1
                else:
                    merged.append(nums[right])
                    right+=1
            while left<=mid:
                merged.append(nums[left])
                left+=1
            while right<=high:
                merged.append(nums[right])
                right+=1
            
            nums[low:high+1]=merged
        return merge_sort(0,len(nums)-1)      