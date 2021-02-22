from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        n1, n2 = len(nums1), len(nums2)
        sumPairs = []
        for j in range(min(n2, k)):
            heappush(sumPairs, (nums1[0] + nums2[j], 0, j))
        
        k = min(n1*n2, k)
        kSumPairs = []
        while k:
            _, i, j = heappop(sumPairs)
            kSumPairs.append([nums1[i], nums2[j]])
            
            if i + 1 < n1:
                heappush(sumPairs, (nums1[i+1]+nums2[j], i+1, j))
            
            k -= 1
        
        return kSumPairs
