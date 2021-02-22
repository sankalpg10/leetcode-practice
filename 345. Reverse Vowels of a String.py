class Solution:
    def reverseVowels(self, s: str) -> str:
        sarr = list(s)
        i, j = 0, len(sarr)-1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while i < j:
            if sarr[i] not in vowels:
                i += 1
            elif sarr[j] not in vowels:
                j -= 1
            else:
                sarr[i], sarr[j] = sarr[j], sarr[i]
                i += 1
                j -= 1
        
        return "".join(sarr)
