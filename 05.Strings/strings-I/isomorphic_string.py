# Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s 
# can be replaced to get t.All occurrences of a character must be replaced with another character while preserving the order 
# of characters.




#Time complexity:O(n)  ,space complexity:O(n)
class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        if len(s)!=len(t):
            return False
        char_s_t={}
        char_t_s={}
        for cs,ct in zip(s,t):
            if cs in char_s_t and char_s_t[cs]!=ct:
                return False
            if ct in char_t_s and char_t_s[ct]!=cs:
                return False
            char_s_t[cs]=ct
            char_t_s[ct]=cs
        return True