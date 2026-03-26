# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase 
# English character. You can perform this operation at most k times.You are given a string s and an integer k. You can choose any
# character of the string and change it to any other uppercase English character. You can perform this operation at most k times.





#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(1)
class Solution(object):
    def characterReplacement(self, s, k):
        max_len=0
        for i in range(len(s)):
            freq={}
            max_freq=0
            for j in range(i,len(s)):
                freq[s[j]]=freq.get(s[j],0)+1
                max_freq=max(max_freq,freq[s[j]])
                change=(j-i+1)-max_freq
                if change<=k:
                    max_len=max(max_len,j-i+1)
                else:
                    break
        return max_len





#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def characterReplacement(self, s, k):
        max_len=0
        freq={}
        max_freq=0
        left=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            max_freq=max(max_freq,freq[s[right]])
            
            while (right-left+1)-max_freq>k:
                freq[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len