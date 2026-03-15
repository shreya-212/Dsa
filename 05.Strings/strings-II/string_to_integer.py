# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.Return the integer as the final result.


#Time complexity:O(n)  ,Space complexity:O(1)
class Solution(object):
    def myAtoi(self, s):
        i=0
        INT_MAX=2**31-1
        INT_MIN=-2**31
        while i<len(s) and s[i]==' ':
            i+=1
        sign=1
        if i<len(s) and (s[i]=='+' or s[i]=='-'):
            if s[i]=='-':
                sign=-1
            i+=1
        num=0
        while i<len(s) and s[i].isdigit():
            digit=int(s[i])
            if num>(INT_MAX-digit)//10:
                return INT_MAX if sign==1 else INT_MIN
            num=num*10+digit
            i+=1
        return sign*num

        