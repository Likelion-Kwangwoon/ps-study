function solution(k, score) {
  const answer = [score[0]]
  let best = [score[0]]
  
  for(let i = 1; i < score.length; i++) {
      if(best.length < k)
          best.push(score[i])
      
      else {
          const minNum = answer.at(-1)
          const minIdx = best.indexOf(minNum)
          
          if(score[i] > minNum) {
              best = [...best.slice(0, minIdx), ...best.slice(minIdx + 1)]
              best.push(score[i])
          }
      }
      
      answer.push(Math.min(...best))
  }
  
  return answer
}