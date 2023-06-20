function solution(ingredient) {
  let count = 0
  let stack = []

  for (let i = 0; i < ingredient.length; i++) {
      stack.push(ingredient[i])

      if (stack.length < 4) continue
      if (stack.at(-4) !== 1) continue
      if (stack.at(-3) !== 2) continue
      if (stack.at(-2) !== 3) continue
      if (stack.at(-1) !== 1) continue
      
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      
      count++
  }

  return count
}