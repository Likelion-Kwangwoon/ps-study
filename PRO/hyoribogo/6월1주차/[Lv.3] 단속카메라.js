function solution(routes) {
  routes.sort((a, b) => a[1] - b[1])
  
  let end = routes[0][1]
  let result = 1
  
  for(const r of routes) {
      if(end < r[0]) {
          end = r[1]
          result++
      }
  }
  
  return result
}