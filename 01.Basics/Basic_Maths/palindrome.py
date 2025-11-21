# You are given an integer n. You need to check whether the number is a palindrome number or not.
#  Return true if it's a palindrome number, otherwise return false.

class Solution:
    def isPalindrome(self, x):
        num=x
        rev=0
        while x>0:
            dig=x%10
            rev=(rev*10)+dig
            x//=10
        return num==rev

