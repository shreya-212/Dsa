# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
# The sorting must be done in-place, without making a copy of the original array.

#Brute force solution -Time complexity:O(n^2),space complexity:O(1)
class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j+1],nums[j]=nums[j],nums[j+1]
        return nums








#Better Solution- Time complexity:O(n),space complexity:O(1)
class Solution(object):
    def sortColors(self, nums):
        count_0=count_1=count_2=0
        for num in nums:
            if num==0:
                count_0+=1
            elif num==1:
                count_1+=1
            else:
                count_2+=1
        index=0
        for _ in range(count_0):
            nums[index]=0
            index+=1
            
        for _ in range(count_1):
            nums[index]=1
            index+=1
        for _ in range(count_2):
            nums[index]=2
            index+=1
        return nums
    







#Optimal Solution - Time complexity:O(n),space complexity:O(1)
class Solution(object):
    def sortColors(self, nums):
        low=mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums







        

        


        