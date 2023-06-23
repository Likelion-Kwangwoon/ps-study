function solution(n) {
  const arr = Array.from({ length: n }, () => new Array(n).fill(null))
  let currRow = 0, currColumn = 0
  let currDirection = 'r'
  
  const isValidRange = num => (num >= n || num < 0) ? false : true
  
  for (let i = 1; i <= n * n; i++) {
      arr[currRow][currColumn] = i
      if (i === n * n) break
      
      if (currDirection === 'r') {
          if (isValidRange(currColumn + 1) && !arr[currRow][currColumn + 1]) {
              currColumn++
              continue
          }
          currDirection = 'd'
      }
      
      if (currDirection === 'd') {
          if (isValidRange(currRow + 1) && !arr[currRow + 1][currColumn]) {
              currRow++
              continue
          }
          currDirection = 'l'
      }
      
      if (currDirection === 'l') {
          if (isValidRange(currColumn - 1) && !arr[currRow][currColumn - 1]) {
              currColumn--
              continue
          }
          currDirection = 'u'
      }
      
      if (currDirection === 'u') {
          if (isValidRange(currRow - 1) && !arr[currRow - 1][currColumn]) {
              currRow--
              continue
          }
          currDirection = 'r'
          i--
      }
  }
  
  return arr
}