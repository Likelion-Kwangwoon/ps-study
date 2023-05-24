function solution(X, Y) {
  const Xcnt = {}
  const Ycnt = {}
  let result = ""
  
  for(const num of X)
      Xcnt[num] = (Xcnt[num] || 0) + 1
      
  for(const num of Y)
      Ycnt[num] = (Ycnt[num] || 0) + 1
  
  for(let i = 9; i >= 0; i--) {
      const num = i.toString()
      result += num.repeat(Math.min(Xcnt[num], Ycnt[num]))
  }
  
  if(result === "") return "-1"
  if(result[0] === "0") return "0"
  return result
}