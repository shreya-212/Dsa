# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
class Solution:
    def reverseNumber(self,n):
        rev=0
        while n>0:
            dig=n%10
            rev=(rev*10)+dig
            n//=10
        return rev


