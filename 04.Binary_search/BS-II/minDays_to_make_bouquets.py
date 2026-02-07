# You are given an integer array bloomDay, an integer m and an integer k.You want to make m bouquets. To make a bouquet, 
# you need to use k adjacent flowers from the garden.Return the minimum number of days you need to wait to be able to make
# m bouquets from the garden. If it is impossible to make m bouquets return -1.

#Brute force solution  -Time complexity:O(n *max(bloomDay))  ,space complexity:O(1)
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m*k>len(bloomDay):
            return -1
        min_day=min(bloomDay)
        max_day=max(bloomDay)
        for day in range(min_day,max_day+1):
            flowers=0
            bouquet=0
            for bloom in bloomDay:
                if bloom<=day:
                    flowers+=1
                    if flowers==k:
                        bouquet+=1
                        flowers=0
                else:
                    flowers=0
            if bouquet>=m:
                return day
        return -1

        
#Optimal solution  -Time complexity:O(n *log max(bloomDay))  ,space complexity:O(1)
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m*k>len(bloomDay):
            return -1
        def possible_bouquet(bloomDay,m,k,day):
            flowers=0
            bouquet=0
            for bloom in bloomDay:
                if bloom<=day:
                    flowers+=1
                    if flowers==k:
                        bouquet+=1
                        flowers=0
                        if bouquet>=m:
                            return True
                else:
                    flowers=0
            return bouquet>=m


        low,high=min(bloomDay),max(bloomDay)
        day=-1
        while low<=high:
            mid=(low+high)//2
            bouquet=possible_bouquet(bloomDay,m,k,mid)
            if bouquet:
                day=mid
                high=mid-1
            else:
                low=mid+1
        return day
            
        
        