# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is 
# the number of times it appears in the string.Return the sorted string. If there are multiple answers, return any of them.




#Time complexity: O(n + k log k), space complexity: O(n)
class Solution(object):
    def frequencySort(self, s):
        result=""
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        sorted_chr=sorted(freq.items(), key=lambda x: x[1],reverse=True)
        for ch,count in sorted_chr:
            result+=ch*count
        return result

        
        