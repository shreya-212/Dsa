# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
# Given a string s, return the sum of beauty of all of its substrings.



#Time complexity:O(n^2)  ,space complexity:O(n)
class Solution(object):
    def beautySum(self, s):
        tot=0
        for i in range(len(s)):
            freq={}
            for j in range(i,len(s)):
                freq[s[j]]=freq.get(s[j],0)+1
                value=freq.values()
                maxi=max(value)
                mini=min(value)
                tot+=(maxi-mini)
        return tot
