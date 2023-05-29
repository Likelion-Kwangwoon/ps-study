class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        dp ={}
        def dfs(r, c):
            #base case
            if r == 1 or c == 1:
                return 1
            
            #memo
            if (r,c) not in dp:
                #reculsive
                dp[(r,c)] = dfs(r-1,c)+ dfs(r,c-1)

            return dp[(r,c)]
        
        return(dfs(m,n))
