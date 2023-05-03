function solution(num, total) {
  const result = []
  const mid = ~~(total / num)
  const gap = ~~(num / 2)
  
  if(num % 2) {
      for(let i = mid - gap; i <= mid + gap; i++)
          result.push(i)
      return result
  }
  for(let i = mid - gap + 1; i <= mid + gap; i++)
      result.push(i)
  return result
}