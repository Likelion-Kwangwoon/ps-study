function solution(n) {
    const num = [];
  
    for (let i = 2; i <= n; i++) {
      num[i] = i;
    }
  
    for (let j = 2; j <= n; j++) {
      if (num[j] === 0) continue;
      for (let k = j + j; k <= n; k += j) {
        num[k] = 0; 
      }
    }
    return num.filter((n) => n).length;
  }