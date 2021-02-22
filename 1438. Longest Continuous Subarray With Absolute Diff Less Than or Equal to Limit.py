class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)
        l, r = 0, 0
        maxLen = 1
        Q = MaxMinQueue()
        while r < n:
            if l == r or abs(nums[r] - Q.max()) <= limit and abs(nums[r] - Q.min()) <= limit:
                Q.append(nums[r])
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                Q.popleft()
                l += 1
        
        return maxLen

from collections import deque
class MaxMinQueue:
    def __init__(self):
        self.Q, self.maxQ, self.minQ = deque(), deque(), deque()
    
    def max(self): return self.maxQ[0]
    
    def min(self): return self.minQ[0]
    
    def append(self, x):
        self.Q.append(x)
        while self.maxQ and self.maxQ[-1] < x: self.maxQ.pop()
        self.maxQ.append(x)
        while self.minQ and self.minQ[-1] > x: self.minQ.pop()
        self.minQ.append(x)
    
    def popleft(self):
        res = self.Q.popleft()
        if self.maxQ[0] == res: self.maxQ.popleft()
        if self.minQ[0] == res: self.minQ.popleft()
        return res
