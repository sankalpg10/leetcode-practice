class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(dotPos):
            if len(dotPos) == 3:
                validIP, ip = validateIP(dotPos)
                if validIP: allIps.add(ip)                  
                return
            
            prevDot = len(dotPos) if not dotPos else dotPos[-1]
            for i in range(prevDot+1, n):
                backtrack(dotPos + [i])
        
        def validateIP(dotPos):
            lastPos = 0
            newip = []
            for pos in dotPos:
                newip.append(s[lastPos:pos])
                lastPos = pos

            newip.append(s[lastPos:])
            for subip in newip:
                if not 0 <= int(subip) <= 255 or (len(subip) > 1 and subip[0]=='0'):
                    return False, None
            return True, ".".join(newip)
        
        n = len(s)
        allIps = set()
        backtrack([])
        return allIps
        
# better way
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def backtrack():
            if len(dots) == 3:
                if isValidIP(s[dots[2]:]):
                    allIps.append(makeIPwithDots())
                return
            
            prevDot = 0 if len(dots) == 0 else dots[-1]
            for currDot in range(prevDot, min(prevDot+3, n-1)):
                if isValidIP(s[prevDot:currDot+1]):
                    dots.append(currDot+1)
                    backtrack()
                    dots.pop()
        
        def isValidIP(t):
            if len(t) > 3 or len(t) == 0: return False
            if len(t) > 1 and t[0] == '0': return False
            return int(t) <= 255
        
        def makeIPwithDots():
            return ".".join([s[:dots[0]], s[dots[0]:dots[1]], s[dots[1]:dots[2]], s[dots[2]:]])
        
        n = len(s)
        allIps = []
        dots = []
        backtrack()
        return allIps
        
