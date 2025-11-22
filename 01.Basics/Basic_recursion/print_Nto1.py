# Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.

class Solution:
    def printNumbers(self, n):
        if n==0:
            return
        print(n)
        self.printNumbers(n-1)
        
        