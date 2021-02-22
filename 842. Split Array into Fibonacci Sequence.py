class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        n = len(S)
        currSeq = []
        maxNum = 2**31 - 1
        def backtrack(ind):
            if len(currSeq) >= 3 and currSeq[-1] != currSeq[-2] + currSeq[-3]:
                return [] # if does not satisfy fibonacii principle return []
            
            if ind >= n:
                if len(currSeq) >= 3: return currSeq # only send the result if result has at least three numbers
                return []
            
            for i in range(ind+1, n+1):
                num = int(S[ind:i])
                if num > maxNum: return [] # num should not be larger than 2**31 - 1
                if (i > ind + 1 and S[ind] == "0"): return [] # if num has 2 or more digits then num should not start with 0
                currSeq.append(num)
                res = backtrack(i)
                if res: return res # if found the solution return solution
                currSeq.pop()
                
        return backtrack(0)
