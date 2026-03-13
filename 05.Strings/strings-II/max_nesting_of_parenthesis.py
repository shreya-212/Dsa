# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 


#Time complexity: O(n)  ,space complexity:O(1)
class Solution(object):
    def maxDepth(self, s):
        max_dept=0
        count=0
        for ch in s:
            if ch=='(':
                count+=1
                max_dept=max(max_dept,count)
            elif ch==')':
                count-=1
        return max_dept
        