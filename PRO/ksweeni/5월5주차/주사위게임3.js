function solution(a, b, c, d) {
    var set = [...new Set([a,b,c,d])];
      
      if (set.length === 1) return set[0] * 1111;
  
      else if (set.length === 2) {
          let arr = [a, b, c, d].sort();
  
          if (arr[0] === arr[1] && arr[0] === arr[2]) {
              return (arr[0] * 10 + arr[3]) ** 2;
          } else if (arr[1] === arr[2] && arr[1] === arr[3]) {
              return (arr[1] * 10 + arr[0]) ** 2;
          } else {
              return (arr[0] + arr[2]) * Math.abs(arr[0] - arr[2])
          }
      } 
          else if (set.length === 3){
          let arr2 = [a, b, c, d].sort();
          if (arr2[0] === arr2[1]){
              return arr2[2] * arr2[3];
          } 
          else if (arr2[1] === arr2[2]){
              return arr2[0] * arr2[3];
          } 
          else if (arr2[2] === arr2[3]) {
              return arr2[0] * arr2[1];
          }
      } 
      else {
          return Math.min(...set);
      }
  }