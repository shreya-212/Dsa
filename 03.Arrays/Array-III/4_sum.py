# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
# such that: a, b, c, and d are distinct and nums[a] + nums[b] + nums[c] + nums[d] == target


#Brute force solution - Time complexity:O(n^4) ,space complexity:O(m)
class Solution(object):
    def fourSum(self, nums, target):
        n=len(nums)
        result=set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for x in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]+nums[x]==target:
                            result.add((nums[i],nums[j],nums[k],nums[x]))
        return [list(quad) for quad in result]
        
        





#Better solution  -Time complexity:O(n^3)  ,space complexity:O(m+n)
class Solution(object):
    def fourSum(self, nums, target):
        n=len(nums)
        nums.sort()
        result=set()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                seen=set()
                for k in range(j+1,n):
                    fourth=target-(nums[i]+nums[j]+nums[k])
                    if fourth in seen:
                        result.add(tuple(sorted((nums[i],nums[j],nums[k],fourth))))
                    else:
                        seen.add(nums[k])
        return [list(quad) for quad in result]
    







#Optimal Solution  -Time complexity:O(n^3)  ,space complexity :O(m)
class Solution(object):
    def fourSum(self, nums, target):
        n=len(nums)
        nums.sort()
        result=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left,right=j+1,n-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total==target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left <right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return result
        

                        

        