class Solution:
    def isHappy(self, n: int) -> bool:
        og = n
        seen = set()
        while n != 1 and n not in seen:
            s = 0
            seen.add(n)
            while n > 0:
                s += (n % 10)**2
                n //= 10
            n = s

        return n == 1
