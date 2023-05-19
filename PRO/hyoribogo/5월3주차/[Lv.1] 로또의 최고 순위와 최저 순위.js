function solution(lottos, win_nums) {
  let minNum = 0, maxNum = 0
  
  for(let i = 5; i >= 0; i--) {
      if(!lottos[i])
          maxNum++
      if(win_nums.includes(lottos[i])) {
          lottos.pop()
          minNum++
      }
  }
  maxNum += minNum
  
  return [Math.min(6, 7 - maxNum), Math.min(6, 7 - minNum)]
}