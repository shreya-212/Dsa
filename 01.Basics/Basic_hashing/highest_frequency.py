# Given an array nums of n integers, find the most frequent element in it.
#  The element that occurs the maximum number of times.

class Solution:
    def mostFrequentElement(self, nums):
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        max_freq=-1
        ans=None
        for key,val in freq.items():
            if val>max_freq:
                max_freq=val
                ans=key
            elif val==max_freq and key<ans:
                ans=key
        return max_freq

            

     