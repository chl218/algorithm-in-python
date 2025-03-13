class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        keySet = set()
        roomsToCheck = set()
        
        keySet.add(0)
        roomsToCheck.update(rooms[0])
        
        while roomsToCheck:
            key = roomsToCheck.pop()    
            keySet.add(key)
            
            for k in rooms[key]:
                if k not in keySet:
                    roomsToCheck.add(k)
            
        for i in range(1, len(rooms)):
            if i not in keySet:
                return False
            
        return True