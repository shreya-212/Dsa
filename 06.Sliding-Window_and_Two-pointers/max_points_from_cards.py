# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the
# integer array cardPoints.Given the integer array cardPoints and the integer k, return the maximum score you can obtain.



#Brute force solution -Time complexity:O(k)  ,space complexity:O(1)
class Solution(object):
    def maxScore(self, cardPoints, k):
        n=len(cardPoints)
        max_score=0
        for i in range(k+1):
            tot=0
            for j in range(i):
                tot+=cardPoints[j]
            for j in range(k-i):
                tot+=cardPoints[n-1-j]
            max_score=max(max_score,tot)
        return max_score
                



#Optimal solution  -Time complexity:O(n)  ,space complexity:O(1)
class Solution(object):
    def maxScore(self, cardPoints, k):
        n=len(cardPoints)
        tot=sum(cardPoints[:k])
        max_score=tot
        for i in range(k):
            tot-=cardPoints[k-1-i]
            tot+=cardPoints[n-i-1]
            max_score=max(max_score,tot)
        return max_score
            