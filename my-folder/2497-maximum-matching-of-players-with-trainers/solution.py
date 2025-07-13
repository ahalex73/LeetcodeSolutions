class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        players.sort()
        trainers.sort()

        player = 0
        trainer = 0
        matches = 0
        
        while(player < len(players) and trainer < len(trainers)):
            if players[player] <= trainers[trainer]:
                player += 1
            
            trainer += 1
        
        return player


