from collections import defaultdict
        
class UndergroundSystem:

    def __init__(self):
        self.timeLog = {}
        self.checkIns = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkIns:
            self.checkIns[id] = []
        self.checkIns[id].append(stationName)
        self.checkIns[id].append(t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInStation, checkInTime = self.checkIns[id]
        if checkInStation not in self.timeLog:
            self.timeLog[checkInStation] = {}
        if stationName not in self.timeLog[checkInStation]:
            self.timeLog[checkInStation][stationName] = [t - checkInTime, 1]
        else:
            self.timeLog[checkInStation][stationName][0] += (t - checkInTime)
            self.timeLog[checkInStation][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.timeLog[startStation][endStation][0]/self.timeLog[startStation][endStation][1]
