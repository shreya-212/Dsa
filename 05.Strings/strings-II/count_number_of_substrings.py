# You are given a string s and a positive integer k.Return the number of substrings that contain exactly k distinct characters.


#Brute force solution  -Time complexity:O(n^2)  ,space complexity:O(n)
def countSub(s,k):
    count=0
    for i in range(len(s)):
        unique=set()
        for j in range(i,len(s)):
            unique.add(s[j])
            if len(unique)==k:
                count+=1
            if len(unique)>k:
                break
    return count





#Optimal solution  -Time complexity:O(n)  ,space complexity:O(n)
class Solution:
    def countSub(self,s,k):
        i=0
        count={}
        res=0
        for j in range(len(s)):
            count[s[j]]=count.get(s[j],0)+1
            while len(count)>k:
                count[s[i]]-=1
                if count[s[i]]==0:
                    del count[s[i]]
                i+=1
            res+=j-i+1
        return res
    def countSubExactlyK(self,s, k):  
        return self.countSub(s,k)-self.countSub(s,k-1)

