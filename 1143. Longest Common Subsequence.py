class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
           a  c  e
        a  3  2  1  0
        b  2  2  1  0
        c  2  2  1  0
        d  1  1  1  0
        e  1  1  1  0
           0  0  0  0
        """
        t1, t2 = len(text1), len(text2)
        DP = [(t2+1)*[0] for _ in range(t1+1)]
        
        for i in range(t1-1, -1, -1):
            for j in range(t2-1, -1, -1):
                if text1[i] == text2[j]: DP[i][j] = 1 + DP[i+1][j+1]
                else: DP[i][j] = max(DP[i][j+1], DP[i+1][j])
                    
        return DP[0][0]
