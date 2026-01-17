# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


#Brute force Solution  -Time complexity:O(n^2) ,space complexity:O(1)
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        result=[]
        for i in range(n):
            count=0
            for j in range(n):
                if nums[j]==nums[i]:
                    count+=1
            if count>(n//3) and nums[i] not in result:
                result.append(nums[i])
        return result








#Better solution - Time complexity:O(n) ,space complexity:O(n)
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        result=[]
        seen={}
        for num in nums:
            seen[num]=seen.get(num,0)+1
        for num,count in seen.items():
            if count>(n//3):
                result.append(num)
        return result









#Optimal Solution : Time complexity- O(n) , space complexity-O(1)
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        count1=count2=0
        major1=major2=None
        result=[]
        for num in nums:
            if num==major1:
                count1+=1
            elif num==major2:
                count2+=1
            elif count1==0:
                count1,major1=1,num
            elif count2==0:
                count2,major2=1,num
            else:
                count1-=1
                count2-=1
        count1=count2=0
        for num in nums:
            if num==major1:
                count1+=1
            elif num==major2:
                count2+=1
        if count1>(n//3):
            result.append(major1)
        if count2>(n//3):
            result.append(major2)
        return result






        




        