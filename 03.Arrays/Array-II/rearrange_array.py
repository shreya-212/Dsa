# Given an integer array nums of even length consisting of an equal number of positive and negative integers.
# Return the answer array in such a way that the given conditions are met


#Brute force solution -Time complexity:O(n^2),space complexity:O(n)
class Solution:
    def rearrangeArray(self, nums):
        n=len(nums)
        res=[0]*n
        used=[False]*n
        for i in range(n):
            if i%2==0:
                for j in range(n):
                    if nums[j]>0 and not used[j]:
                        res[i]=nums[j]
                        used[j]=True
                        break
            else:
                for j in range(n):
                    if nums[j]<0 and not used[j]:
                        res[i]=nums[j]
                        used[j]=True
                        break
        return res

        





#Better Solution - Time complexity:O(n),space complexity:O(n)
class Solution(object):
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        k=j=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=pos[k]
                k+=1
            else:
                nums[i]=neg[j]
                j+=1
        return nums
    


#Optimal Solution -Time complexity:O(n),space complexity:O(n)
class Solution(object):
    def rearrangeArray(self, nums):
        res=[0]*len(nums)
        pos=0
        neg=1
        for num in nums:
            if num>0:
                res[pos]=num
                pos+=2
            else:
                res[neg]=num
                neg+=2
        return res