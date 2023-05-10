function solution(n, works) {
  if(works.reduce((a, c) => a + c) <= n) return 0
  
  works.sort((a, b) => b - a)
  
  while(n) {
    const max = works[0]
    
    for(let i = 0; i < works.length; i++) {
      if(works[i] >= max) {
        works[i]--
        n--
      }
      if(!n) break
    }
  }
  
  return works.reduce((a, c) => a + c**2, 0);
}