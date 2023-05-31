function solution (A, B) {
  let answer = 0
  
  A.sort((a, b) => b - a)
  B.sort((a, b) => a - b)
  
  for(const a of A) {
    if(a < B.at(-1)) {
      answer++
      B.pop()
    }
  }
  
  return answer
}