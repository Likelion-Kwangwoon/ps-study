function solution(numbers) {
  const nums = [...numbers]
  const max = +([...nums].sort((x, y) => y - x).join(""))
  const primeArr = primes(max)
  let count = 0
  for (const item of primeArr) {
    const arr = [...item.toString()]
    if (isTrue(arr, nums)) count++
  }
  return count
}

const isTrue = (arr, nums) => {
  const copy = [...nums]
  for (const item of arr) {
    const index = copy.indexOf(item)
    if (index === -1) {
      return false
    }
    copy.splice(index, 1)
  }
  return true
}

const primes = max => {
  const arr = [2]
  for (let i = 3; i <= max; i += 2) {
    let isPrime = true
    const sqrt = Math.sqrt(i);
    for (const item of arr) {
      if (item > sqrt) {
        break
      }
      if (i % item === 0) {
        isPrime = false
        break
      }
    }
    if (isPrime) arr.push(i)
  }
  return arr
}