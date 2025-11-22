# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers.
# Return the GCD of the two numbers

class Solution:
    def GCD(self, n1, n2):
        while n2!=0:
            n1,n2=n2,n1%n2
        return n1
