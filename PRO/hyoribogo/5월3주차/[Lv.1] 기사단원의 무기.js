function solution(number, limit, power) {
  let result = 1
  for(let i = 2; i <= number; i++) 
      result += cntDiv(i) > limit ? power : cntDiv(i)
  return result
}

function cntDiv(n) {
  let cnt = 0
  for(let i = 1; i < Math.sqrt(n); i++)
      cnt += !(n % i) ? 2 : 0
  if(Number.isInteger(Math.sqrt(n)))
      cnt++
  return cnt
}