class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       
        dp ={}
        def dfs(r, c):
            if r == 1 or c == 1:
                return 1
            
            if (r,c) not in dp:
                dp[(r,c)] = dfs(r-1,c)+ dfs(r,c-1)
            
            return dp[(r,c)]
        
        return(dfs(m,n))
