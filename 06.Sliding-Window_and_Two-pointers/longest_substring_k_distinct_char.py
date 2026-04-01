



#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(n)
class Solution:
    def kDistinctChar(self, s, k):
        max_len=0
        for i in range(len(s)):
            check=set()
            for j in range(i,len(s)):
                if s[j] not in check:
                    check.add(s[j])
                if len(check)>k:
                    break
                if len(check)==k:
                    max_len=max(max_len,j-i+1)
        return max_len
