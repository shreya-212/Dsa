# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character
# in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".


#Brute Force solution : time complexity:O(m^2*n) , space complexity:O(m+n)
class Solution(object):
    def minWindow(self, s, t):
        min_len=float('inf')
        result=""
        count_t={}
        for ch in t:
            count_t[ch]=count_t.get(ch,0)+1
        for i in range(len(s)):
            freq_sub={}
            for j in range(i,len(s)):
                freq_sub[s[j]]=freq_sub.get(s[j],0)+1
                valid=True
                for ch in count_t:
                    if freq_sub.get(ch,0)<count_t[ch]:
                        valid=False
                        break
                if valid:
                    if(j-i+1)<min_len:
                        min_len=j-i+1
                        result=s[i:j+1]
        return result
    



#Optimal solution  : time complexity:O(m+n)  ,space complexity:O(m+n)
class Solution(object):
    def minWindow(self, s, t):
        minlen=float('inf')
        result=""
        count_t={}
        for ch in t:
            count_t[ch]=count_t.get(ch,0)+1
        left=0
        freq={}
        have=0
        need_cnt=len(count_t)
        for right in range(len(s)):
            ch=s[right]
            freq[ch]=freq.get(ch,0)+1

            if ch in count_t and freq[ch]==count_t[ch]:
                have+=1
            while have==need_cnt:

                if right-left+1<minlen:
                    minlen=right-left+1
                    result=s[left:right+1]

                freq[s[left]]-=1
                if s[left] in count_t and freq[s[left]]<count_t[s[left]]:
                    have-=1
                left+=1
        return result
                
            


        


        