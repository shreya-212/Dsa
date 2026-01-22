# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.




#Brute force solution -Time complexity :O(n^3) ,space complexity:O(n)
class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        merged=True
        while merged:
            merged=False
            n=len(intervals)
            for i in range(n):
                for j in range(i+1,n):
                    a,b=intervals[i]
                    c,d=intervals[j]
                    
                    if not (b<c or d<a):
                        intervals[i]=[min(a,c),max(b,d)]
                        intervals.pop(j)
                        merged=True
                        break
                if merged:
                    break
        return intervals
            
    







#Optimal solution  -Time comeplexity:O(n log n) ,space complexity:O(n)  
class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x :x[0])
        merged=[intervals[0]]
        for start,end in intervals[1:]:
            cur_start,cur_end=merged[-1]
            if start<=cur_end:
                merged[-1][1]=max(cur_end,end)
            else:
                merged.append([start,end])
        return merged