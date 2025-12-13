
#Brute force Solution - Time complexity:O(n),space complexity:O(n)
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
    