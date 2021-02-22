class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        noteCount = collections.Counter(ransomNote)
        magCount = collections.Counter(magazine)
        
        for letter in noteCount:
            if letter not in magCount or magCount[letter] < noteCount[letter]:
                return False
            
        return True
            
