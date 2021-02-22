class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if len(s) == 0: return True # return True if string is empty
        self.words = set(wordDict) # convert wordDict array to set for fast lookup
        self.startDict = collections.defaultdict(set) # create a dictionary where keys are starting letters of each word in wordDict and values are set/array of words that start with key as their starting letter
        for word in self.words:
            self.startDict[word[0]].add(word)
        self.memo = {} # a memoization hashmap to keep track of words that we have already know are in or not in the wordDict
        
        return self.dfs(s)
        
    def dfs(self, s):
        if s in self.memo: return self.memo[s] # if word is in memo return that value
        if s in self.words: return True # if word is in wordDict return True
        result = False # make a flag result that would turn true if given word is in the memo or wordDict
        if s[:1] in self.startDict: # we check if the first letter is in startDict if not return False coz we can never make a word which start from this letter.
            # Note here we could have used s[0] but it would throw an error when len(s) == 0
            prefixes = self.startDict[s[0]] # get all the word that starts from letter s[0]
            for prefix in prefixes: # iterate over those prefixes
                if prefix == s[:len(prefix)]: # if the given prefix is equal to the subword of string s starting from start upto len(prefix)
                    # then check if the rest of the string can be made using words given in wordDict
                    result = self.dfs(s[len(prefix):])
                if result: # if result is True then no need to check further and return True else continue and check if it works with other prefixes
                    self.memo[s] = True # save to memo
                    return True
            
            self.memo[s] = False # if all prefixes fail return False and save to memo
        return False

    
    # Slower solution
    class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.words = set(wordDict)
        self.memo = {}
        return self.dfs(s)
        
    def dfs(self, s):
        if s in self.memo: return self.memo[s]
        if s in self.words: return True
        result = False
        for i in range(1, len(s)):
            result = self.dfs(s[:i]) and self.dfs(s[i:])
            if result:
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False
    
   
# Tabulation
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #leetcode
        n = len(s)
        DP = [False]*(n+1)
        DP[n] = True
        for i in range(n-1, -1, -1):
            for w in wordDict:
                isPrefix = i + len(w) <= n and w == s[i:i+len(w)]
                if isPrefix and DP[i+len(w)]: 
                    DP[i] = True
                    break
        return DP[0]
