# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, 
# and + represents string concatenation.Return s after removing the outermost parentheses of every primitive string in the 
# primitive decomposition of s.




#  Time complexity:O(n)  ,space complexity:O(n)
class Solution(object):
    def removeOuterParentheses(self, s):
        count=0
        result=[]
        for ch in s:
            if ch=='(':
                if count>0:
                    result.append(ch)
                count+=1
            else:
                count-=1
                if count>0:
                    result.append(ch)
        return "".join(result)
        