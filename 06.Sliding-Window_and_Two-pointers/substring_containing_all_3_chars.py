# Given a string s consisting only of characters a, b and c.Return the number of substrings containing at least one 
# occurrence of all these characters a, b and c.



#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(n)
class Solution(object):
    def numberOfSubstrings(self, s):
        count=0
        for i in range(len(s)):
            freq={'a':0,'b':0,'c':0}
            for j in range(i,len(s)):
                if s[j] in freq:
                    freq[s[j]]+=1
                if freq['a']>0 and freq['b']>0 and freq['c']>0:
                    count+=len(s)-j
                    break
        return count








#Optimal solution -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def numberOfSubstrings(self, s):
        count=0
        left=0
        freq={'a':0,'b':0,'c':0}
        for right in range(len(s)):
            freq[s[right]]+=1
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                count+=len(s)-right
                freq[s[left]]-=1
                left+=1
        return count