class Solution:
    def minInsertions(self, s: str) -> int:
        """
            m b a d m
          j 0 1 2 3 4  
        i     
        0   0 1 2 3 2
        1   0 0 1 2 3
        2   0 0 0 1 2
        3   0 0 0 0 1
        4   0 0 0 0 0
            
        base case:
        for string of length 1: 0 i.e. DP[i][i] = 0
        for string of length 2: if both chars match then 0 else 1, 
            i.e. if s[i] == s[j]: DP[i][i+1] = 0
                 else: DP[i][i+1] = 1

        general case:
            if s[i] == s[j]:
                DP[i][j] = DP[i+1][j-1] # amount of correction required of string of currlength - 2
            else:
                DP[i][j] = 1 + min(DP[i+1][j], DP[i][j-1])
                               min of correction required without last char and correction required without first character
            
        """
        
        n = len(s)
        DP = [[0]*n for _ in range(n)]
        for i in range(n-1):
            if s[i] != s[i+1]: DP[i][i+1] = 1
        
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                if s[i] == s[j]: DP[i][j] = DP[i+1][j-1]
                else: DP[i][j] = 1 + min(DP[i+1][j], DP[i][j-1])
        
        return DP[0][-1]
