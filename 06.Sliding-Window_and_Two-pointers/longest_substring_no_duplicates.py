# Given a string s, find the length of the longest substring without duplicate characters.





#Brute force Solution -Time complexity:O(n^2)  ,space complexity:O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest=0
        for i in range(len(s)):
            check=set()
            for j in range(i,len(s)):
                if not s[j] in check:
                    check.add(s[j])
                    length=j-i+1
                    longest=max(longest,length)
                else:
                    break
        return longest
             


