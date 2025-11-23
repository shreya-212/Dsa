# Given an array nums of size n which may contain duplicate elements.
# Return a list of pairs where each pair contains a unique element from the array and its frequency in the array.

class Solution:
    def countFrequencies(self, nums):
        freq={}
        res=[]
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
        for key,val in freq.items():
            res.append([key,val])
        return res



