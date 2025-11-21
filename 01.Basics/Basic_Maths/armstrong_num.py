# You are given an integer n. You need to check whether it is an armstrong number or not.
# Return true if it is an armstrong number, otherwise return false.

class Solution:
    def isArmstrong(self, n):
        digit=len(str(n))
        num=n
        tot=0
        while n>0:
            dig=n%10
            tot+=(dig**digit)
            n//=10
        return num==tot

            
           


            
        