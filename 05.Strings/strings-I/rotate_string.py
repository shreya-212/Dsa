# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.


#Brute force solution  -Time complexity:O(n^2) ,space complexity:O(n)
class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        for  i in range(len(s)):
            rotate=s[i:]+s[:i]
            if rotate==goal:
                return True
        return False





#Optimal Solution  -Time complexity:O(n)  ,space complexity:O(n)
class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        con=s+s
        if goal in con:
            return True
        return False