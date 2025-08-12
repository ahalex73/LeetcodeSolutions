class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # n = number of people
        # time = time -> one second passes per pass 
        # Return the index of the person holding the pillow after time seconds

        # Partition solution

        # lets take example of n = 5
        # 1 2 3 4 5 | 5 4 3 2 1 | 1 2 3 4 5 | 5 4 3 2 1 | 1 2 3 4 5 
        # The odd-th chunk starts with 1, whilst the even-th chunk starts with number n

        # time // (n - 1)

        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))
        
    
