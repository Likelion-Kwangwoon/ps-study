function solution(n, stations, w) {
  let result = 0
  const range = w * 2 + 1
  let diff = 0

  if (stations[0] - w > 1)
    result += Math.ceil((stations[0] - w - 1) / range)

  if (stations.at(-1) + w < n)
    result += Math.ceil((n - (stations.at(-1) + w)) / range)

  for (let i = 0; i < stations.length - 1; i++) {
    diff = stations[i + 1] - stations[i] - (2 * w) - 1
    result += Math.ceil(diff / range)
  }

  return result
}