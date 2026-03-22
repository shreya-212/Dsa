# Given a string s, find the length of the longest substring without duplicate characters.





#Brute force Solution -Time complexity:O(n^2)  ,space complexity:O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest=0
        for i in range(len(s)):
            check=set()
            for j in range(i,len(s)):
                if s[j] not in check:
                    check.add(s[j])
                    length=j-i+1
                    longest=max(longest,length)
                else:
                    break
        return longest
             






#Optimal solution  -Time complexity:O(n) ,space complexity:O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len=0
        i=0
        seen={}
        for j in range(len(s)):
            if s[j] in seen:
                i=max(i,seen[s[j]]+1)
            seen[s[j]]=j
            max_len=max(max_len,j-i+1)
        return max_len
