class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        opened = set()
        def dfs(roomID):
            
            for key in rooms[roomID]:
                if key not in opened:
                    opened.add(key)
                    dfs(key)
        
        opened.add(0)
        dfs(0)
        return len(opened) == len(rooms)
