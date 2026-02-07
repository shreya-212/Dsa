# There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.Each hour, 
# she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.Return the minimum integer k such that she can eat all the bananas within h hours.



#Brute force solution  -Time complexity:O(n *max(piles)) ,space complexity:O(1)
class Solution(object):
    def minEatingSpeed(self, piles, h):
        def find_hrs(piles,k):
            total_hrs=0
            for pile in piles:
                total_hrs+=(pile+k-1)//k
            return total_hrs
        m=max(piles)
        for i in range(1,m+1):
            tot_hr=find_hrs(piles,i)
            if tot_hr<=h:
                return i
        



#Optimal solution  -Time complexity:O(n* log max(piles))) ,space complexity:O(1)
class Solution(object):
    def minEatingSpeed(self, piles, h):
        def find_hrs(piles,k):
            total_hrs=0
            for pile in piles:
                total_hrs+=(pile+k-1)//k
            return total_hrs
        
        low,high=1,max(piles)
        ans=0
        while low<=high:
            mid=(low+high)//2
            tot_hr=find_hrs(piles,mid)
            if tot_hr<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans






