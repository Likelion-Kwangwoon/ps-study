function solution(a, b, c, d) {
  if(a === b && b === c && c === d) return a * 1111
  
  const dice = [a, b, c, d].sort()
  
  if((dice[0] + dice[1] + dice[2]) / 3 === dice[0]) return (10 * dice[0] + dice[3])**2
  if((dice[1] + dice[2] + dice[3]) / 3 === dice[1]) return (10 * dice[1] + dice[0])**2
  
  if(dice[0] === dice[1] && dice[2] === dice[3]) return (dice[0] + dice[2]) * Math.abs(dice[0] - dice[2])
  if(dice[0] !== dice[1] && dice[1] !== dice[2] && dice[2] !== dice[3]) return dice[0]
  
  for(let i = 0; i < 3; i++) {
      if(dice[i] === dice[i + 1]) {
          dice[i] = 1
          dice[i + 1] = 1
      }
  }
  
  return dice[0] * dice[1] * dice[2] * dice[3]
}