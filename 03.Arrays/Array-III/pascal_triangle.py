# Given two integers r and c, return the value at the rth row and cth column (1-indexed) in a Pascal's Triangle.


#Time complexity  :O(min(r,c)) ,space complexity: O(1)
class Solution:
    def pascalTriangleI(self, r, c):
        n=r-1
        k=c-1
        k=min(k,n-k)
        result=1
        for i in range(k):
            result=result*(n-i)//(i+1)
        return result