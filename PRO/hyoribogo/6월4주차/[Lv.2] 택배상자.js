function solution(order) {
  order.reverse()
  let answer = 0
  const stack = []
  const main = Array.from({ length: order.length }, (_, i) => order.length - i)
  
  while (order.length) {
      if (main.at(-1) === order.at(-1)) {
          main.pop()
          order.pop()
          answer++
          continue
      }
      
      if (stack.at(-1) === order.at(-1)) {
          stack.pop()
          order.pop()
          answer++
          continue
      }
      if (stack.at(-1) !== order.at(-1) && !main.length) break
      stack.push(main.pop())
  }
  
  return answer
}