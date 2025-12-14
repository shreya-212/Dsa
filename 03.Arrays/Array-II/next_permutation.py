# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# Return the next permutation of an array of integers ,the next lexicographically greater permutation of its integer.


#Brute force Solution -Time comlplexity:O(n!*n log(n!)),space complexity:O(n!*n)
from itertools import permutations
class Solution(object):
    def nextPermutation(self, nums):
        perm=sorted(set(permutations(nums)))
        curr=tuple(nums)
        indx=perm.index(curr)
        if indx==len(perm)-1:
            next_perm=perm[0]
        else:
            next_perm=perm[indx+1]
        nums[:]=list(next_perm)









#Optimal Solution -Time complexity:O(n),space complexity:O(1)
class Solution(object):
    def nextPermutation(self, nums):
        n=len(nums)
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j=n-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=reversed(nums[i+1:])