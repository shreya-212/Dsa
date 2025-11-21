# You are given an integer n. You need to find all the divisors of n. 
# Return all the divisors of n as an array or list in a sorted order
class Solution:
    def divisors(self, n):
        res=[]
        for i in range(1,n+1):
            if n%i==0:
                res.append(i)
        return res
