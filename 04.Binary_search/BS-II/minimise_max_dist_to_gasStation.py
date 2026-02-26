# Given a sorted array arr of size n, containing integer positions of n gas stations on the X-axis, and an integer k, place k new gas 
# stations on the X-axis.Let dist be the maximum distance between adjacent gas stations after adding the k new gas stations.
# Find the minimum value of dist.



# time complexity:O(n log(maximum distance/precision))  ,space complexity:O(1)
import math
class Solution:
    def minimiseMaxDistance(self, arr, k):
        def required_station(dist):
            station=0
            for i in range(len(arr)-1):
                gap=arr[i+1]-arr[i]
                station+=math.ceil(gap/dist)-1
            return station
        low,high=1e-6,arr[-1]-arr[0]
        while high-low> 1e-6:
            mid=(low+high)/2
            if required_station(mid)>k:
                low=mid
            else:
                high=mid
        return high
            
            
