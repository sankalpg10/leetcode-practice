class Solution:
    def numDecodings(self, s: str) -> int:
        """
        "1 1 1 0 6"
                   i
        [1 1 2 3 2 2]
        at index i I am checking how many ways can I decode the string from 0 to i-1. If digit at i-1 is 0 then the digit i-2 and i-1 would combine to make a single number so we would fetch the interpretation of the string from 0 to i-2(not inclusive) and use that
        Forward Recurrence
        Base Case:
        DP[0] = 1
        DP[1] = 0 if DP[0] == '0' else 1
        
        General Case:
        if s[i] == '0': DP[i] = DP[i-1]
        if valid(s[i-2:i]): DP[i] += DP[i-2]
        
        """
        if s[0] == '0': return 0
        n = len(s)
        DP = [0]*(n+1)
        
        DP[0] = 1
        DP[1] += s[0] != '0'
        
        for i in range(2, n+1):
            
            if s[i-1] != '0':
                DP[i] = DP[i-1]
            
            twoDigits = int(s[i-2:i])
            if 10 <= twoDigits <= 26:
                DP[i] += DP[i-2]
        print(DP)
        return DP[-1]
