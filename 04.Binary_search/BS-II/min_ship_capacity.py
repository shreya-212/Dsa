# A conveyor belt has packages that must be shipped from one port to another within days days.The ith package on the conveyor 
# belt has a weight of weights[i]. Return the least weight capacity of the ship that will result in all the packages on the
# conveyor belt being shipped within days days.


#Brute force soluton  -Time complexity:O(n *sum(weights))  ,space complexity:O(1)
class Solution(object):
    def shipWithinDays(self, weights, days):
        for x in range(max(weights),sum(weights)+1):
            curr_weight=0
            day=1
            for w in weights:
                if curr_weight+w<=x:
                    curr_weight+=w
                else:
                    day+=1
                    curr_weight=w
            if day<=days:
                return x




#Optimal Solution  -Time complexity:O(n* log(sum(weights)))  ,space complexity:O(1)
class Solution(object):
    def shipWithinDays(self, weights, days):
        def days_needed(capacity):
            day=1
            curr_weight=0
            for w in weights:
                if curr_weight+w<=capacity:
                    curr_weight+=w
                else:
                    day+=1
                    curr_weight=w
            return day
            
        
        low,high=max(weights),sum(weights)
        while low<high:
            mid=(low+high)//2
            day=days_needed(mid)
            if day<=days:
                high=mid
            else:
                low=mid+1
        return low

             


