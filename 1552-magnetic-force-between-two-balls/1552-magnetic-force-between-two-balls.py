class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Step 1: ALWAYS sort the positions first!
        position.sort()
        
        # Step 2: The Helper Function (Greedy Placement)
        def can_place(dist: int) -> bool:
            count = 1                 # Put 1st ball in first basket
            last_pos = position[0]    # Track where we placed the last ball
            
            for i in range(1, len(position)):
                # If this basket is far enough from our last ball:
                if position[i] - last_pos >= dist:
                    count += 1
                    last_pos = position[i]
                    
                    # Quick exit if we've placed all required balls
                    if count >= m:
                        return True
                        
            return count >= m

        # Step 3: Binary Search on Answer
        lo = 1                                  # Smallest possible distance
        hi = position[-1] - position[0]         # Maximum possible distance
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if can_place(mid):
                ans = mid        # It worked! Save this distance
                lo = mid + 1     # We want the MAXIMUM, so try guessing BIGGER!
            else:
                hi = mid - 1     # Too big, couldn't place m balls. Guess SMALLER!
                
        return ans