class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        i, j = 0, len(people)-1
        numVisits = 0
        while i <= j:
            numVisits += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            
        return numVisits
    
    def withoutSorting(self, people, limit):
        weights = collections.defaultdict(int)
        for wt in people:
            weights[wt] += 1
        maxwt, minwt = max(people), min(people)
        numTurns = 0
        while minwt <= maxwt:
            if weights[maxwt] > 0:
                numTurns += 1
                weights[maxwt] -= 1
                if minwt + maxwt <= limit:
                    weights[minwt] -= 1
            else:
                maxwt -= 1
            
            while weights[minwt] == 0 and minwt < maxwt:
                minwt += 1
                
        return numTurns
        
