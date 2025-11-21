# You are given an integer n. You need to return the number of digits in the number.
# The number will have no leading zeroes, except when the number is 0 itself.
class Solution:
    def countDigit(self,n):
        count=0
        while n>0:
            dig=n%10
            count+=1
            n//=10
        return count
s=Solution()
print(s.countDigit(14))
