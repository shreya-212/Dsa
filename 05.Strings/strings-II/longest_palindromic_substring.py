# Given a string s, return the longest palindromic substring in s.


#Brute force solution  -Time complexity:O(n^3)  ,space complexity:O(1)
class Solution(object):
    def longestPalindrome(self, s):
        max_len=0
        longest=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                check=s[i:j+1]
                if check==check[::-1]:
                    if len(check)>max_len:
                        max_len=len(check)
                        longest=check
        return longest
    





#Better solution  -Time complexity:O(n^2)  ,space complexity:O(1)
class Solution(object):
    def expand(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    def longestPalindrome(self, s):
        longest=""
        for i in range(len(s)):
            odd=self.expand(s,i,i)
            even=self.expand(s,i,i+1)
            if len(odd)>len(longest):
                longest=odd
            if len(even)>len(longest):
                longest=even
        return longest



                

        
        