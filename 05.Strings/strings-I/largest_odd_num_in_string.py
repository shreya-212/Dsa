# You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a 
# non-empty substring of num, or an empty string "" if no odd integer exists.


#Brute force solution   -Time complexity:O(n^3)  ,space complexity:O(1)
class Solution:  
    def largeOddNum(self, s: str) -> str:
        largest=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub=s[i:j+1]
                if int(sub[-1])%2==1:
                    if largest=="" or int(sub)>int(largest):
                        largest=sub

        return largest




#Optimal Solution  - Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def largestOddNumber(self, num):
        indx=-1
        for i in range(len(num)-1,-1,-1):
            if (int(num[i])%2)==1:
                indx=i
                break
        j=0
        while j<=indx and num[j]=='0':
            j+=1
        return num[j:indx+1]
            