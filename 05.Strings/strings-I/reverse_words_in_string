# Given an input string s, reverse the order of the words.A word is defined as a sequence of non-space characters. 
# The words in s will be separated by at least one space.Return a string of the words in reverse order concatenated by a
# single space.


#Brute force solution  -Time complexity:O(n)  ,space complexity:O(n)
class Solution(object):
    def reverseWords(self, s):
        words=[]
        word=""
        for ch in s:
            if ch!=" ":
                word+=ch
            elif word:
                words.append(word)
                word=""

        if word:
            words.append(word)
        words.reverse()
        return " ".join(words)
        



#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def reverseWords(self, s):
        result=""
        i=len(s)-1
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            if i<0:
                break
            end=i
            while i>=0 and s[i]!=" ":
                i-=1
            word=s[i+1:end+1]
            if result!="":
                result+=" "
            result+=word
        return result