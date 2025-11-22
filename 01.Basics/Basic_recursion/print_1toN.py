# Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.

class Solution:
    def printNumbers(self, n):
        if n==0:
            return
        self.printNumbers(n-1)
        print(n)
