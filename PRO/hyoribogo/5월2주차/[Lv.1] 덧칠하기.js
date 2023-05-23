function solution(n, m, section) {
  let answer = 0
  let endLine = 0
  for(const s of section) {
      if(!endLine || endLine < s) {
          answer++
          endLine = s + m - 1
      }
  }
  return answer
}