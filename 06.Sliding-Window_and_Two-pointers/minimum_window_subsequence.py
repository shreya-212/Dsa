# Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.




# Brute Force Solution  - Time complexity:O(n^3) ,space complexity:O(n)
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        minlen=float('inf')
        result=""
        for i in range(len(s1)):
            for j in range(i,len(s1)):
                k=0
                for x in range(i,j+1):
                    if k<len(s2) and s1[x] ==s2[k]:
                        k+=1
                        if k==len(s2):
                            break
                if k==len(s2):
                    if j-i+1<minlen:
                        minlen=j-i+1
                        result=s1[i:j+1]
                    break
        return result
    







#Optimal solution  -Time complexity:O(n*m)  ,space complexity:O(1)
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n,m=len(s1),len(s2)
        minlen=float('inf')
        start=-1
        scan1=0
        while scan1<n:
            scan2=0
            while scan1<n:
                if s1[scan1]==s2[scan2]:
                    scan2+=1
                    if scan2==m:
                        break
                scan1+=1
            if scan2<m:
                break
            end=scan1+1
            scan2-=1
            while scan2>=0:
                if s1[scan1]==s2[scan2]:
                    scan2-=1
                scan1-=1
            scan1+=1
            if end-scan1<minlen:
                minlen=end-scan1
                start=scan1
            scan1+=1
        return "" if start==-1 else s1[start:start+minlen]
            











        
