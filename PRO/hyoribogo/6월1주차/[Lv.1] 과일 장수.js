function solution(k, m, score) {
  let result = 0
  score.sort((a, b) => b - a).forEach((v, i) =>
      result += !((i + 1) % m) ? v * m : 0)
  return result
}