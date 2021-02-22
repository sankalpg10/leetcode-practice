class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = {}
        self.arrList = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hashMap: return False
        
        self.hashMap[val] = len(self.arrList)
        self.arrList.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hashMap: return False
        
        ind = self.hashMap[val]
        self.arrList[-1], self.arrList[ind] = self.arrList[ind], self.arrList[-1]
        self.hashMap[self.arrList[ind]] = ind
        self.arrList.pop()
        del self.hashMap[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return choice(self.arrList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
