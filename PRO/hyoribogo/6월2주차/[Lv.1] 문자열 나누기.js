function solution(s) {
  let answer = 0
  let cnt = 1
  let start = s[0]
  
  for(let i = 1; i < s.length; i++) {
      if(!cnt) {
          cnt++
          start = s[i]
          continue
      }
      if(start === s[i]) cnt++
      else cnt--
          
      if(!cnt) answer++
  }
  if(cnt) answer++
  return answer
}