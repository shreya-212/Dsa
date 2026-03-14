# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.Given a roman numeral, convert it to an integer.




#Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def romanToInt(self, s):
        value={
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        res=0
        for i in range(len(s)-1):
            if value[s[i]]<value[s[i+1]]:
                res-=value[s[i]]
            else:
                res+=value[s[i]]
        return res+value[s[-1]]
        