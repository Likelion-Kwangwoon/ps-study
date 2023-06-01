function solution(arr, query) {
  query.forEach((idx, i) => {
      if(i % 2)
          arr.splice(0, idx)
      else
          arr.splice(idx + 1)
  })
  
  return arr
}