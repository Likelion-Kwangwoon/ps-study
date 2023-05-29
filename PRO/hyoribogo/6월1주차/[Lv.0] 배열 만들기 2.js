function solution(l, r) {
  const zerofive = []
  let result = []
  
  const dfs = (num, end) => {
      if(+num > r) return
      zerofive.push(+num)
      
      dfs(num + "0", end)
      dfs(num + "5", end)
  }
  dfs(5, r)
  
  zerofive.sort((a, b) => a - b)
  for(let i = 0; i < zerofive.length; i++) {
      if(zerofive[i] >= l) {
          result = zerofive.slice(i)
          break
      }
  }
  
  return result.length ? result : [-1]
}