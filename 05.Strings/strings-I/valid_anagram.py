# Given two strings s and t, return true if t is an anagram of s, and false otherwise.



#Brute force solution  -Time complexity:O(n log n)  ,space complexity:O(1)
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)






#Better solution  -Time complexity:O(n)  ,space complexity:o(n)
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count_s={}
        count_t={}
        for ch in s:
            count_s[ch]=count_s.get(ch,0)+1
        for ch in t:
            count_t[ch]=count_t.get(ch,0)+1
        return count_s==count_t
        





#Optimal solution  -Time complexity:O(n)  ,space complexity:O(n)
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count_check={}
        for ch in s:
            count_check[ch]=count_check.get(ch,0)+1
        for ch in t:
            if ch not in count_check:
                return False
            count_check[ch]-=1
            if count_check[ch]<0:
                return False
        return True
