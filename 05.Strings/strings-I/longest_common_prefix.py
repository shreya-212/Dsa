# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

#Brute force solution  -Time complexity:O(n*m^2)  ,space complexity:O(1)
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=""
        for i in range(len(strs[0])):
            prefix+=strs[0][i]
            for s in strs:
                if not s.startswith(prefix):
                    return prefix[:-1]
        return prefix
            




#Better solution  -Time complexity:O(n log n*m) ,dpsce complexity:O(1)
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first=strs[0]
        last=strs[-1]
        i=0
        while i<len(first) and first[i]==last[i]:
            i+=1
        return first[:i]
    






#Optimal solution  -Time complexity:O(n*m)  ,space complexity:O(1)
class Solution(object):
    def longestCommonPrefix(self, strs):
        minlen=float('inf')
        for s in strs:
            if len(s)<minlen:
                minlen=len(s)
        i=0
        while i<minlen:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]
