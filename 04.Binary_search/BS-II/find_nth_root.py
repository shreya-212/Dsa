# Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that
# when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.





#Brute force solution  -Time complexity:O(m)  ,space complexity:O(1)
class Solution:
    def NthRoot(self, n, m):
        for i in range(m+1):
            if i**n==m:
                return i
        return -1





#Optimal solution  -Time complexity:O(log m *log n)  ,space complexity:O(1)

class Solution:
    def NthRoot(self, n, m):
        def power(num,n,m):
            result=1
            while n>0:
                if n%2==1:
                    result*=num
                    if result>m:
                        return result
                num*=num
                n//=2
            return result
        if m==0 or m==1 or n==1:
            return m
        low,high=1,m
        while low<=high:
            mid=(low+high)//2
            pow_val=power(mid,n,m)
            if pow_val==m:
                return mid
            elif pow_val<m:
                low=mid+1
            else:
                high=mid-1
        return -1

      
      