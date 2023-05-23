class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        N = len(cost)
        def top_down(N):
            if N == 0:
                dp[0] = cost[0]
                return dp[0]
            if N == 1:
                dp[1] = cost[1]
                return dp[1]

            
            if N == len(cost):
                return min(top_down(N-1), top_down(N-2))

            # Top -down
            if N not in dp:
                dp[N]= cost[N] + min(top_down(N-1) ,top_down(N-2))
        
            return dp[N]

        ans =top_down(N)



        return(ans)