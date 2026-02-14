# You are given A painters and an array C of N integers where C[i] denotes the length of the ith board. 
# Each painter takes B units of time to paint 1 unit of board.The goal is to minimize the time to paint all boards


#Brute force solution  -Time complexity:O(n*sum(C)) ,space complexity:O(1)
class Solution:
    def paint(self, A, B, C):
        def count_painter(time):
            painter=1
            cur_sum=0
            for num in C:
                if cur_sum+num<=time:
                    cur_sum+=num
                else:
                    painter+=1
                    cur_sum=num
            return painter
        for x in range(max(C),sum(C)+1):
            mod=10000003
            painter=count_painter(x)
            if painter<=A:
                return (x*B)%mod








#Optimal solution  -Time complexity:O(n*log(sum(C)))  ,space complexity:O(1)
class Solution:
    def paint(self, A, B, C):
        def count_painter(time):
            painter=1
            cur_sum=0
            for num in C:
                if cur_sum+num<=time:
                    cur_sum+=num
                else:
                    painter+=1
                    cur_sum=num
            return painter
        low,high=max(C),sum(C)
        ans=0
        mod=10000003
        while low<=high:
            mid=(low+high)//2
            painter=count_painter(mid)
            if painter<=A:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return (ans*B)%mod
          