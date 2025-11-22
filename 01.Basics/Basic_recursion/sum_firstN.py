# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

class Solution:
    def NnumbersSum(self, N):
        if N==0:
            return 0
        return N +self.NnumbersSum(N-1) 
