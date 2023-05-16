function solution(begin, target, words) {
  // words 안에 target이 없으면 0 반환
  if(!words.includes(target)) return 0

  const visited = new Array(words.length).fill(false)
  let result = []
      
  const dfs = (change, cnt) => {
      if(change === target) {
          result.push(cnt)
      }
      
      const fw = words.filter(word => {
          let diffCnt = 0
          for(let i = 0; i < word.length; i++) {
              diffCnt += word[i] !== change[i] ? 1 : 0
          }
          return diffCnt === 1 && !visited[words.indexOf(word)]
      })
      
      if(!fw.length) return
      
      fw.forEach(word => {
          visited[words.indexOf(word)] = true
          dfs(word, cnt + 1)
      })
  }
  
  dfs(begin, 0)
  return Math.min(...result)
}