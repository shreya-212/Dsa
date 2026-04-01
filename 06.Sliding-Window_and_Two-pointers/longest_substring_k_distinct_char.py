# Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.



#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(n)
class Solution:
    def kDistinctChar(self, s, k):
        max_len=0
        for i in range(len(s)):
            check=set()
            for j in range(i,len(s)):
                check.add(s[j])
                if len(check)>k:
                    break
                if len(check)==k:
                    max_len=max(max_len,j-i+1)
        return max_len






#Optimal solution  -Time complexity:O(n)  ,space complexity:O(k)
class Solution:
    def kDistinctChar(self, s, k):
        max_len=0
        left=0
        freq={}
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while len(freq)>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            if len(freq)==k:
                max_len=max(max_len,right-left+1)
        return max_len