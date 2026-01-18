# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.Notice that the solution set must not contain duplicate triplets.





#Brute force solution - Time complexity:O(n^3) ,space complexity:O(n^2)
class Solution(object):
    def threeSum(self, nums):
        n=len(nums)
        result=set()
        for i in range(n):
            for j in range(i+1,n):
                for x in range(j+1,n):
                    if nums[i]+nums[j]+nums[x]==0:
                        result.add(tuple(sorted((nums[i],nums[j],nums[x]))))
        return list(result)







#Better Solution - Time complexity:O(n^2) ,space complexity:O(n^2)
class Solution:
    def threeSum(self, nums):
        n=len(nums)
        nums.sort()
        result=set()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            seen=set()
            for j in range(i+1,n):
                third=-(nums[i]+nums[j])
                if third in seen:
                    result.add(tuple(sorted((nums[i],nums[j],third))))
                else:
                    seen.add(nums[j])
        return [list(triplet) for triplet in result]
    











#Optimal Solution - Time complexity:O(n^2) , space complexity:O(1)
class Solution(object):
    def threeSum(self, nums):
        n=len(nums)
        nums.sort()
        result=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return result




        